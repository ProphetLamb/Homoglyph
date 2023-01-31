# Homoglyphs

Namespace: Homoglyph

A homoglyph is one of two or more glyphs with shapes that appear identical or very similar.

```csharp
public static class Homoglyphs
```

Inheritance [Object](https://docs.microsoft.com/en-us/dotnet/api/system.object) → [Homoglyphs](./homoglyph.homoglyphs.md)

**Remarks:**

Data taken from https://github.com/codebox/homoglyph/blob/master/raw_data/char_codes.txt

## Methods

### **GetHomoglyphs(Char)**

For any given utf-8 glyph determines the associated homoglyphs.

```csharp
public static ReadOnlySpan<uint> GetHomoglyphs(char codepoint)
```

#### Parameters

`codepoint` [Char](https://docs.microsoft.com/en-us/dotnet/api/system.char)<br>
The utf-8 glyph to probe.

#### Returns

[ReadOnlySpan&lt;UInt32&gt;](https://docs.microsoft.com/en-us/dotnet/api/system.readonlyspan-1)<br>

### **GetHomoglyphs(UIntPtr)**

For any given utf-32 glyph determines the associated homoglyphs.

```csharp
public static ReadOnlySpan<uint> GetHomoglyphs(UIntPtr codepoint)
```

#### Parameters

`codepoint` [UIntPtr](https://docs.microsoft.com/en-us/dotnet/api/system.uintptr)<br>
The utf-32 glyph to probe.

#### Returns

[ReadOnlySpan&lt;UInt32&gt;](https://docs.microsoft.com/en-us/dotnet/api/system.readonlyspan-1)<br>
