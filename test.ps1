$dir = (Get-Item $pwd).FullName + "\src"
dotnet test --no-restore --no-build --test-adapter-path:$dir --logger:Appveyor /p:AltCover='true' /p:AltCoverAssemblyExcludeFilter='^(?!Homoglyph).*$|Test.*$'

foreach ($coverage in Get-ChildItem -Recurse -File coverage*.xml) {
    # postprocess the coverage files
    $coverage_xml = [xml](Get-Content $coverage.FullName)
    $coverage_xml.CoverageSession.Modules.Module | % {
        if ($_.ModuleName -match '^(?!Homoglyph).*$|Test.*$') {
            $_.ParentNode.RemoveChild($_)
        }
        if ($_.skippedDueTo -eq 'Filter') {
            $_.ParentNode.RemoveChild($_)
        }

        $_.Files.File | % {
            if ($_.fullPath -match '^[\\/]_[\\/]') {
                $_.fullPath = $_.fullPath -replace '^[\\/]_[\\/]', ''
            }
            else {
                $_.ParentNode.RemoveChild($_)
            }
        }
    }
    # 3. trim $pwd from /CoverageSession/Modules/Module/ModulePath
    $coverage_xml.CoverageSession.Modules.Module | % {
        $_.ModulePath = $_.ModulePath -replace [regex]::escape($dir), ''
    }
    # wirte the changes back to the file
    $coverage_xml.Save($coverage.FullName)

    $commitID = & git rev-parse HEAD
    $commitBranch = & git rev-parse --abbrev-ref HEAD

    & csmacnz.Coveralls --useRelativePaths --basePath $dir --opencover -i $coverage --commitId $commitID --commitBranch $commitBranch
}
