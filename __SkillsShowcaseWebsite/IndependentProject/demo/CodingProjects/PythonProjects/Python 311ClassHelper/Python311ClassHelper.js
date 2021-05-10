const output = document.getElementById("output")
const code = document.getElementById("code")

code.addEventListener("keydown", function (event) {
    if (event.ctrlKey && event.key === "Enter") {
        evaluatePython()
    }
})

function addToOutput(s) {
    output.value += `>>>${code.value}\n${s}\n`
    output.scrollTop = output.scrollHeight
    code.value=''
}

output.value = 'Initializing...\n'
// init pyodide
languagePluginLoader.then(() => { output.value += 'Ready!\n' })

function evaluatePython() {
    pyodide.runPythonAsync(code.value)
        .then(output => addToOutput(output))
        .catch((err) => { addToOutput(err) })
}
