proc external_editor {filename linenumber} {
	exec code -g "$filename:$linenumber" &
	return
}

set PrefSource(altEditor) external_editor