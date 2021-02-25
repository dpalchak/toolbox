proc external_editor {filename linenumber} {
	exec "C:/Windows/System32/cmd.exe" /C "code -g $filename:$linenumber" &
	return
}

set PrefSource(altEditor) external_editor