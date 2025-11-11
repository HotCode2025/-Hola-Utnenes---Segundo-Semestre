<template>
  <footer class="footer">
    <p class="footer-contacto">Contacto:</p>
    <div class="icon-links">
      <a href="mailto:tuemail@gmail.com" target="_blank" class="gmail">
        <i class="fas fa-envelope"></i> Gmail
      </a>
      <a href="https://github.com/tuusuario" target="_blank" class="github">
        <i class="fab fa-github"></i> GitHub
      </a>
      <a href="https://linkedin.com/in/tuusuario" target="_blank" class="linkedin">
        <i class="fab fa-linkedin"></i> LinkedIn
      </a>
      <a href="https://docs.google.com/forms/d/tuformulario" target="_blank" class="formulario">
        <i class="fas fa-file-alt"></i> Formulario
      </a>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #7f00ff;
  color: black;
  text-align: center;
  padding: 20px;
  box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.6);
  margin-top: 50px;
}

.footer-contacto {
  font-size: 2.2rem;
  font-weight: bold;
  margin-bottom: 15px;
}

.icon-links {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 35px;
  margin-top: 10px;
}

.footer a {
  text-decoration: none;
  font-weight: bold;
  font-size: 2.1rem;
  transition: color 0.3s;
  display: flex;
  align-items: center;
  gap: 8px;
}


.footer a.gmail i {
  color: #D44638; 
}

.footer a.github i {
  color: #333; 
}

.footer a.linkedin i {
  color: #0077B5; 
}

.footer a.formulario i {
  color: #0F9D58; 
}

.footer a:hover {
  color: white;
}

.footer i {
  margin-right: 8px;
}

@media (max-width: 768px) {
  .footer-contacto {
    font-size: 1.8rem;
  }
  .footer a {
    font-size: 1.8rem;
  }
}

@media (max-width: 480px) {
  .footer-contacto {
    font-size: 1.5rem;
  }
  .footer a {
    font-size: 1.5rem;
  }
}
</style>
