from fasthtml.components import *
from fasthtml.svg import *

content = Style('* {\n    margin: 0;\n    padding: 0;\n    box-sizing: border-box;\n  }\n\n  body {\n    margin: 0;\n    padding: 0;\n    overflow: hidden;\n    height: 100vh;\n    background: radial-gradient(circle, #1b2735, #090a0f);\n  }\n\n  canvas {\n    display: block;\n    position: absolute;\n    top: 0;\n    left: 0;\n    width: 100%; /* Ensure  the width */\n    height: 100%; /* Ensure canvas fully covers the height */\n  }')

Body(
    Canvas(id='cosmosCanvas'),
    Script('const canvas = document.getElementById("cosmosCanvas");\n    const ctx = canvas.getContext("2d");\n\n    function resizeCanvas() {\n      canvas.width = window.innerWidth;\n      canvas.height = window.innerHeight;\n    }\n\n    resizeCanvas();\n    window.addEventListener("resize", resizeCanvas);\n\n    const particles = [];\n    const numParticles = 100;\n\n    class Particle {\n      constructor(x, y, radius, speed) {\n        this.x = x;\n        this.y = y;\n        this.radius = radius;\n        this.speed = speed;\n        this.angle = Math.random() * Math.PI * 2;\n      }\n\n      update() {\n        this.x += Math.cos(this.angle) * this.speed;\n        this.y += Math.sin(this.angle) * this.speed;\n\n        // Bounce off edges\n        if (this.x < 0 || this.x > canvas.width)\n          this.angle = Math.PI - this.angle;\n        if (this.y < 0 || this.y > canvas.height) this.angle = -this.angle;\n      }\n\n      draw() {\n        ctx.beginPath();\n        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);\n        ctx.fillStyle = "rgba(255, 255, 255, 0.8)";\n        ctx.fill();\n      }\n    }\n\n    // Initialize particles\n    for (let i = 0; i < numParticles; i++) {\n      particles.push(\n        new Particle(\n          Math.random() * canvas.width,\n          Math.random() * canvas.height,\n          Math.random() * 4 + 1,\n          Math.random() * 0.5 + 0.2\n        )\n      );\n    }\n\n    // Connect particles\n    function connectParticles() {\n      for (let a = 0; a < particles.length; a++) {\n        for (let b = a + 1; b < particles.length; b++) {\n          const dist = Math.hypot(\n            particles[a].x - particles[b].x,\n            particles[a].y - particles[b].y\n          );\n\n          if (dist < 120) {\n            ctx.strokeStyle = `rgba(255, 255, 255, ${1 - dist / 120})`;\n            ctx.lineWidth = 0.7;\n            ctx.beginPath();\n            ctx.moveTo(particles[a].x, particles[a].y);\n            ctx.lineTo(particles[b].x, particles[b].y);\n            ctx.stroke();\n          }\n        }\n      }\n    }\n\n    // Animation Loop\n    function animate() {\n      ctx.clearRect(0, 0, canvas.width, canvas.height);\n      particles.forEach((particle) => {\n        particle.update();\n        particle.draw();\n      });\n      connectParticles();\n      requestAnimationFrame(animate);\n    }\n\n    // Start Animation\n    animate();')
)