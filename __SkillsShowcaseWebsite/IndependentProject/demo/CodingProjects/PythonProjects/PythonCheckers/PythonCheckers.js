//https://medium.com/swlh/python-in-web-easy-5f7de3813055
pyodide.js
languagePluginLoader.then()
console.log(pyodide.runPython('import sys; sys.version'))

python_code = `
from js import document
div = document.createElement('div')
div.innerHTML = '<h1>This element was created from Python</h1>'
#insert into body as a first child
document.body.prepend(div)
`
pyodide.runPythonAsync(python_code)
  .then(output => console.log(output))


/*
pyodide.loadPackage('numpy').then(() => {
    // numpy is now available
    pyodide.runPython('import numpy as np')
    console.log(pyodide.runPython('np.ones((3, 3)))'))
})
*/