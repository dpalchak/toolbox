proc external_editor {filename linenumber} {
	exec code-helper.sh -g "$filename:$linenumber" &
	return
}

set PrefSource(altEditor) external_editor