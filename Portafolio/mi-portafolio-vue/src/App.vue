<script setup>
import NavBar from './components/NavBar.vue'
import Estudios from './components/Estudios.vue'
import Experiencia from './components/Experiencia.vue'
import Habilidades from './components/Habilidades.vue'
import Proyectos from './components/Proyectos.vue'
import SiteFooter from './components/SiteFooter.vue'
import SobreMi from './components/SobreMi.vue'

// Referencia explícita a imports para evitar warnings del linter sobre
// variables no usadas cuando el template las consume (script setup).
const __components = [NavBar, SobreMi, Estudios, Experiencia, Habilidades, Proyectos, SiteFooter]
void __components
</script>

<template>
  <div id="app">
    <NavBar />

    <main>
      <SobreMi />

      <!-- Secciones principales (componentes) -->
      <Estudios />
      <Experiencia />
      <Habilidades />
      <Proyectos />

      <section id="contacto">
        <h2>Contacto</h2>
        <p class="contact-subtle">Si preferís, también podés escribirme directamente a <a href="mailto:serenadelvalle25@gmail.com">serenadelvalle25@gmail.com</a></p>
        <div class="formulario-container">
          <iframe
            src="https://docs.google.com/forms/d/e/1FAIpQLSeqLha4ZW0h_NfPmAdfOPsqjZIJoaBniDKyJOw1AOdB4GrkPg/viewform?embedded=true"
            width="100%"
            height="420"
            frameborder="0"
            marginheight="0"
            marginwidth="0"
            loading="lazy"
          >
            Cargando…
          </iframe>
        </div>
      </section>
    </main>

    <SiteFooter />
  </div>
</template>

<style>

</style>


