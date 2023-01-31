$dir = (Get-Item $pwd).FullName + "\src"
dotnet test --no-restore --no-build --test-adapter-path:$dir --logger:Appveyor /p:AltCover='true' /p:AltCoverAssemblyExcludeFilter='^(?!Homoglyph).*$|Test.*$'

$commitID = & git rev-parse HEAD
$commitBranch = & git rev-parse --abbrev-ref HEAD

foreach ($coverage in Get-ChildItem -Recurse -File coverage*.xml) {
    # postprocess the coverage files
    $coverage_xml = [xml](Get-Content $coverage.FullName)
    # 1. fix the `filePath` attributes at xpath = /CoverageSession/Modules/Module/Files/File/@fullPath by removing the leading `/_/`
    $coverage_xml.CoverageSession.Modules.Module.Files.File | % {
        if ($_.fullPath -match '^[\\/]_[\\/]') {
            $_.fullPath = $_.fullPath -replace '^[\\/]_[\\/]', ''
        }
        else {
            $_.ParentNode.RemoveChild($_)
        }
    }
    # 2. remove all nodes with a `skippedDueTo="Filter"` attribute at xpath = /CoverageSession/Modules/Module/@skippedDueTo
    $coverage_xml.CoverageSession.Modules.Module | % {
        if ($_.skippedDueTo -eq 'Filter') {
            $_.ParentNode.RemoveChild($_)
        }
    }
    # 3. trim $pwd from /CoverageSession/Modules/Module/ModulePath
    $coverage_xml.CoverageSession.Modules.Module.ModulePath = $coverage_xml.CoverageSession.Modules.Module.ModulePath -replace [regex]::escape($dir), ''
    # wirte the changes back to the file
    $coverage_xml.Save($coverage.FullName)

    & csmacnz.Coveralls --useRelativePaths --basePath $dir --opencover -i $coverage --commitId $commitID --commitBranch $commitBranch
}
