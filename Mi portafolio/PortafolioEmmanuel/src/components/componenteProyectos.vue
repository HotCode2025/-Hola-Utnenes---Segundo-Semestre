<template>
  <section class="fade-up proyectos">
    <h2>Proyectos</h2>

    <div class="proyecto">
      <h3>Primer semestre</h3>
      <p>Proyecto grupal desarrollado durante el primer semestre de la carrera.</p>
      <a
        href="https://portafolio-grupal-holamundo.netlify.app"
        target="_blank"
        rel="noopener noreferrer"
        class="btn"
      >
        Ver Proyecto
      </a>
    </div>
  </section>
</template>

<style scoped>
.proyectos {
  text-align: center;
  padding: 2rem;
  color: #0a2a43;
}

.proyecto {
  background: #f4f9ff;
  border-radius: 12px;
  padding: 1.5rem;
  margin: 1rem auto;
  max-width: 600px;
  box-shadow: 0 3px 10px rgba(0, 100, 255, 0.1);
}

h2 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: #003366;
}

.btn {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.6rem 1.2rem;
  background: #0056b3;
  color: white;
  border-radius: 8px;
  text-decoration: none;
  transition: background 0.3s ease;
}

.btn:hover {
  background: #003f88;
}
</style>