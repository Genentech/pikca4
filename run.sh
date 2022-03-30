#!/usr/bin/env bash

file=${1:-../../SQLiteParser.g4}

runp () {
    pushd grammar-a4/py
    pygrun \
     ANTLRv4 grammarSpec -tree "${file}"
    popd
}

runj () {
    pushd grammar-a4/java
    java -Xmx500M -cp "/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig \
     ANTLRv4 grammarSpec -tree -gui "${file}"
    popd
}

runj $@
