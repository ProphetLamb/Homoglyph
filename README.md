# Homoglyph

> In orthography and typography, a homoglyph is one of two or more graphemes, characters, or glyphs with shapes that appear identical or very similar.
[Wikipedia](https://en.wikipedia.org/wiki/Homoglyph)

## Usage

Allows the user to retrieve all homoglyphs for a specific utf-32 code-point as a `ReadOnlySpan<uint>`.

```csharp
using Homoglyph;

ReadOnlySpan<uint> codepoints = Homoglyphs.GetHomoglyphs('\u0020'); // &nbsp;
Console.WriteLine(codepoints.Contains(' ') ? "Yay" : "Nope");
// Output: Yay
```

## [API documentation](./doc/Homoglyph/index.md)

## Behind the scenes

The library embeds a Homoglyph hash table into its DLL .text section. A specific feature that allows us to load byte sized data is used. If a property exposes a array of `byte` or `sbyte` as a `ReadOnlySpan<byte>`, then the array is not allocation on the heap a 2nd time, but loaded directly from the dll .text section.

The [following IL](https://sharplab.io/#v2:C4LglgNgNAJiDUAfAAgJgAwFgBQaCMOOyeAnABQDCAdAAoDa6AugJQDcReAbAARrcXcA3jm6jeAZl5duAJQCmAQxgB5AHYQAngGUADgtUAeAEYbgcgHzca3ALyXVcgO7cTZuoyHd0ADwxRuAL7s2AFAA) is generated for such a property getter.
```csharp
using System;

Console.WriteLine(C.P[0]);
static class C {
    public static ReadOnlySpan<byte> P => new byte[] { 0x20, };
}
```

```asm
IL_0000: ldsflda uint8 '<PrivateImplementationDetails>'::'36A9E7F1C95B82FFB99743E0C5C4CE95D83C9A430AAC59F84EF3CBFAB6145068'
IL_0005: ldc.i4.1
IL_0006: newobj instance void valuetype [System.Runtime]System.ReadOnlySpan`1<uint8>::.ctor(void*, int32)
IL_000b: ret
```

Currently, no array allocation is performed. If we were to replace `byte` with `nuint` or most other primitives a separate array would be allocated and filled inline.

```asm
IL_0000: ldc.i4.1
IL_0001: newarr [System.Runtime]System.UIntPtr
IL_0006: dup
IL_0007: ldc.i4.0
IL_0008: ldc.i4.s 32
IL_000a: conv.i
IL_000b: stelem.i
IL_000c: call valuetype [System.Runtime]System.ReadOnlySpan`1<!0> valuetype [System.Runtime]System.ReadOnlySpan`1<native uint>::op_Implicit(!0[])
IL_0011: ret
```

### Hash map

The native shape of homoglyph groupings would be a array of dynamic sized arrays of codepoints.
```csharp
uint[][] homoglyphs = new uint[][] {
	new uint[] { 20,a0,1680,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,200a,2028,2029,202f,205f },
	new uint[] { ... },
};
```
Lookup of any given group is `O(n)` with `n` the sum of the number of codepoints over all groups. Additionally it would require many separate heap allocations.

The first step is to flatten this array into a 1-dimensional structure, by concatenating all groupings.
We note down the start index and length of each group in a separate array.

```csharp
nuint[] homoglyph_flat = new uint[] { 20,a0,1680,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,200a,2028,2029,202f,205f, ... };
(ushort Index, byte Length)[] homoglyph_indexer = new[] { ((ushort)0, (byte)18), ...};
```

This memory optimization brings us down to two allocations, but lookup remains inefficient.

In order to optimize the lookup we reshape `homoglyph_flat` into a new array of $8419$ items inserting at a index using a hash function. This same index is then used to store the index and length data. The resulting hash table has a fill of $6184 / 8419 ~= 73%$.

On this table a hash lookup using the `codepoint` as its own hash value yields the index and length inside the `homoglyph_flat` array. The slice of the array then represents the entire grouping.

```csharp
uint[] blockValues = new uint[] { 20,a0, ... };
uint[] hashValues = new uint[] { 0, 0, 0, ... };
ushort[] hashIndices = new ushort[] { 0, 0, 0, ... };
byte[] hashIndices = new byte[] { 0, 0, 0, ... };

public static ReadOnlySpan<uint> GetHomoglyphs(uint codepoint) {
	int prediction = codepoint % 8419;
	while (true) {
		if (hashValues[prediction] == codepoint) {
			ushort index = hashIndicies[prediction];
			byte length = hashLengths[prediction];
			return blockValues[index..(index + length)];
		}
		if (predictionCount <= HashCapacity) {
			prediction = (prediction + 1) % 8419;
			continue;
		}

		return default;
	}
}
```

Further optimization requires the embedding the arrays into the DLL .text section, optimizing the probing algorithm, the modulo calculation for 64bit platforms, and preventing probing bound checks for array access when possible.

The result of this optimization can be found in [Homoglyph.cs](./src/Homoglyph.cs)
