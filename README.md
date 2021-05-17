<!---->

# How To Run The Program: |
-------------|
Step 1:  Download as a .zip file |
Step 2: Open the folder  ResumeSkillsShowcaseWebsite-main |
Step 3: Open the folder  __SkillsShowcaseWebsite |
Step 4: Open the folder IndependentProjectV2.0 |
Step 5: Click on the index.html file to open it, or drag it into your preferred internet browser. |


# Basic Flow of How I Built This Monstrosity. |
--------------------------------|
Step 1: added background 
'''
<div id="tsparticles"></div>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/tsparticles/1.18.1/tsparticles.min.js" integrity="sha512-PYHWDEuXOTJ9MZ+/QHqkbgiEYZ+LImQv3i/9NyYOABFvK37e4q4Wg7aQDN1JpoGiEu1TYZh6JMrZluZox2gbDA==" crossorigin="anonymous"> </script>
      <script> 
        const particles = {
        "particles": {
          "number": {
            "value": 67,
            "density": {
              "enable": true,
              "value_area": 800
            }
          },
          "color": {
            "value": "#f0ff05"
          },
          "shape": {
            "type": "triangle",
            "stroke": {
              "width": 0,
              "color": "#000000"
            },
            "polygon": {
              "nb_sides": 5
            },
            "image": {
              "src": "img/github.svg",
              "width": 100,
              "height": 300
            }
          },
          "opacity": {
            "value": 0.5,
            "random": false,
            "anim": {
              "enable": false,
              "speed": 1,
              "opacity_min": 0.1,
              "sync": false
            }
          },
          "size": {
            "value": 3,
            "random": true,
            "anim": {
              "enable": false,
              "speed": 40,
              "size_min": 0.1,
              "sync": false
            }
          },
          "line_linked": {
            "enable": true,
            "distance": 150,
            "color": "#ffffff",
            "opacity": 0.4,
            "width": 1
          },
          "move": {
            "enable": true,
            "speed": 0.306824121731046,
            "direction": "none",
            "random": false,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {
              "enable": false,
              "rotateX": 600,
              "rotateY": 1200
            }
          }
        },
        "interactivity": {
          "detect_on": "canvas",
          "events": {
            "onhover": {
              "enable": true,
              "mode": "repulse"
            },
            "onclick": {
              "enable": true,
              "mode": "push"
            },
            "resize": true
          },
          "modes": {
            "grab": {
              "distance": 400,
              "line_linked": {
                "opacity": 1
              }
            },
            "bubble": {
              "distance": 400,
              "size": 40,
              "duration": 2,
              "opacity": 8,
              "speed": 3
            },
            "repulse": {
              "distance": 0.00000000000000000001,
              "duration": 0.4
            },
            "push": {
              "particles_nb": 4
            },
            "remove": {
              "particles_nb": 2
            }
          }
        },
        "retina_detect": true
      };
        tsParticles.load('tsparticles', particles); 
      </script>
'''   |
![Webpage with background &navbar](img/background.png)
Step 2: added navbar
'''
<body>
  <!--Navbar-->
  <!--w3School dropdown navbar-->
  <nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container-fluid">
      <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>                        
        </button>
        <a class="navbar-brand" href="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.bridgemi.com%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Ffull_width_image%2Fpublic%2FPPT-Ohio-pic-4-26.jpg%3Fitok%3D98m1HnbT&imgrefurl=https%3A%2F%2Fwww.bridgemi.com%2Fmichigan-health-watch%2Fall-forgiven-ohio-thanks-covid-vaccine-sincerely-michigan&tbnid=bgoxqWc29qTPMM&vet=12ahUKEwjY5JDdncjwAhWRFqwKHR5sBpwQMygtegUIARDiAQ..i&docid=pMPFHWYe5BHi0M&w=1300&h=712&q=ohio&safe=strict&ved=2ahUKEwjY5JDdncjwAhWRFqwKHR5sBpwQMygtegUIARDiAQ">Degeneracy Inc.</a>
      </div>
      <div>
        <div class="collapse navbar-collapse" id="myNavbar">
          <ul class="nav navbar-nav">
            <li><a href="index.html">Home</a></li>
            <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="CodingProjectsLandingPage.html">Coding Projects<span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="JavaSection.html">Java</a></li>
                <li><a href="PythonSection.html">Python</a></li>
                <li><a href="HTMLSection.html">HTML</a></li>
              </ul>
            </li>
            <li><a href="AboutMe.html">About Me</a></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</body>
![Webpage with background &navbar](img/navbar.png)
'''   |
Step 3: Added in container & text with formatters to make the content of the webpage.   |
Step 4: Added the code viewer windows.   |




# What are the known bugs? |
---------------------------|
1.\) If you resize the window, \(depending on the aspect ratio\) the background won't cover the full window. |
2.\) Python code displayer sometimes won't load |




# Credits: |
---------|
https://stackoverflow.com/questions/25654845/how-can-i-create-a-text-box-for-a-note-in-markdown - automatic! |
https://github.com/VincentGarreau/particles.js/ - automatic! |
                               |
*Rest of sources in code* |





