<script setup>
import NavBar from './components/NavBar.vue'
import Educacion from './components/Educacion.vue'
</script>

<template>
  <header>
    <h1>Matías Tobares</h1>
    <p>Tecnicatura Universitaria en Programación – UTN</p>
    <h3><span>Portafolio Web — Vue 3 + Vite</span></h3>
  </header>

  <NavBar />

  <main>
    <section id="inicio" class="intro">
      <h2>¡Bienvenido!</h2>
      <p>
        Este sitio será mi portafolio personal. En las próximas clases voy a agregar secciones
        como Educación, Experiencia, Proyectos y Contacto.
      </p>
      <p><small>Visitas de prueba: 1</small></p>
    </section>

    <!-- Educación -->
    <Educacion />
  </main>
</template>

<style scoped>
header { text-align: center; margin: 1.2rem 0; }
h1 { font-size: 2.4rem; margin: 0; }
h3 span { color: #42b883; }
.intro { background: #f6f8fa; border-radius: 8px; padding: 1.2rem; }
section { padding: 2rem 0; border-bottom: 1px solid #eaeaea; }
section h2 { color: #42b883; }
</style>
