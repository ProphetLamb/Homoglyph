namespace Homoglyph.Test;

public class HomoglyphsTests {
    [Test]
    public void TestAccessFirstGroup() {
        Homoglyphs.GetHomoglyphs(0x20).ToArray().Should().BeEquivalentTo(new[] { 0x20, 0xa0, 0x1680, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200a, 0x2028, 0x2029, 0x202f, 0x205f });
    }
    [Test]
    public void TestAccessFirstGroupChar() {
        Homoglyphs.GetHomoglyphs('\u0020').ToArray().Should().BeEquivalentTo(new[] { 0x20, 0xa0, 0x1680, 0x2000, 0x2001, 0x2002, 0x2003, 0x2004, 0x2005, 0x2006, 0x2007, 0x2008, 0x2009, 0x200a, 0x2028, 0x2029, 0x202f, 0x205f });
    }

    [Test]
    public void TestAccessContainsChar() {
        ReadOnlySpan<uint> codepoints = Homoglyphs.GetHomoglyphs('\u0020'); // &nbsp;
        codepoints.Contains(' ').Should().BeTrue();
    }

    [Test]
    public void TestAccessLastGroup() {
        Homoglyphs.GetHomoglyphs(0x2a600).ToArray().Should().BeEquivalentTo(new[] { 0x2a600, 0x2fa1d });
        Homoglyphs.GetHomoglyphs(0x2fa1d).ToArray().Should().BeEquivalentTo(new[] { 0x2a600, 0x2fa1d });
    }
}
