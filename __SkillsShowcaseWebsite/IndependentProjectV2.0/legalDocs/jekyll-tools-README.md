[Trinket Jekyll Tools](http://trinketapp.github.io/jekyll-tools/)
====================

Check out our sample Jekyll site [Trinket Jekyll Tools](http://trinketapp.github.io/jekyll-tools/)

Include interactive trinkets in your Jekyll site with 2 lines of code.  Why?  Because static sites are better when they're interactive!  

Trinkets are designed for teaching but you can use them whenever you want your readers to see your code work interactively.  

## Usage

After installation, make your code blocks interactive and awesome with just two additional lines:

```
{% include trinket-open %}
# your code here
{% include trinket-close %}
```

That's it!  As of Sept 2014 Jekyll Tools supports Python and HTML/CSS.

## Python

This code:
```
{% include trinket-open type='python' %}
import turtle

tina = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue']:
    tina.color(c)
    tina.forward(75)
    tina.left(90)

tina.penup()
tina.backward(100)
tina.write("Hello world!")
{% include trinket-close %}

```
Gives you this interactive Python trinket on your Jekyll site:

![](https://trinket.io/api/files/540a1c063dd837df5415c56b/Screenshot-2014-09-05-at-4-16-19-PM.png)

Note: This is just a screenshot.  See the real thing in action [here](http://trinketapp.github.io/jekyll-tools/#python).

## HTML

This code:

```
{% include trinket-open type='html' %}
<html>
<head>
    <style type="text/css">
        body {
            background-color: #008aff;
            text-align: center;
        }
        .logo {
            position: relative;
            top: 50%;
            transform: translateY(-60%);
        }
        .logo img {
            max-width: 90%;
        }
    </style>
</head>
<body>
    <div class="logo">
        <img src="https://trinket.io/img/trinket-logo-big.png" />
    </div>
</body>
</html>
{% include trinket-close %}

```
Gives you this interactive HTML trinket  on your Jekyll site:

![](https://trinket.io/api/files/540a1bf83dd837df5415c56a/Screenshot-2014-09-05-at-4-17-47-PM.png)

Note: These trinkets support most of HTML and CSS, but not Javascript (yet).  Also, you can find a live version of the trinket above [here](http://trinketapp.github.io/jekyll-tools/#html).

## Customize!

Make your trinkets the right height:
```
{% include trinket-open type='python' height='100' %}
for i in range(10):
    print "Only the lines you need"
{% include trinket-close %}

```
Gives you this interactive Python trinket:

![](https://trinket.io/api/files/540a1bec3dd837df5415c569/Screenshot-2014-09-05-at-4-19-27-PM.png)

## Installation

Drop the `trinket-open` and `trinket-close` files into the `_includes` folder of your Jekyll site.

If you're lazy, here's a one-liner you can run from the root of your Jekyll project:

```bash
wget -P _includes https://raw.githubusercontent.com/trinketapp/jekyll-tools/master/_includes/trinket-close https://raw.githubusercontent.com/trinketapp/jekyll-tools/master/_includes/trinket-open
```

## Acknowledgements

Our interactive Python trinket makes heavy use of the awesome [Skulpt project](http://skulpt.org), which uses client side Javascript to interpret Python in your browser.  Check em out and [contribute on Github](http://github.com/skulpt/skulpt)!  

The interactive HTML trinket is soulmates with [Mozilla Thimble](https://thimble.webmaker.org), which is another awesome project that you can [contribute to on Github](https://github.com/mozilla/thimble.webmaker.org).

## Contributions

Contributions to these tools are welcome.  [Contact us](mailto:hello@trinket.io) or open an issue to discuss what you want to do.

## License

Released under the MIT License. (C) 2014 Ben Wheeler.  See LICENSE for details.
