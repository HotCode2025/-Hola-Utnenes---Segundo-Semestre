<template>
  <NavBar />
  <Header />

  <main>
    <section id="educacion">
      <Educacion />
    </section>

    <section id="experiencia">
      <Experiencia />
    </section>

    <section id="proyectos">
      <Proyectos />
    </section>

    <section id="habilidades">
      <Habilidades />
    </section>

    <section id="intereses">
      <Intereses />
    </section>
  </main>

  <Footer />
</template>

<script setup>
import NavBar from './components/NavBar.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

import Educacion from './components/Educacion.vue'
import Experiencia from './components/Experiencia.vue'
import Proyectos from './components/Proyectos.vue'
import Habilidades from './components/Habilidades.vue'
import Intereses from './components/Intereses.vue'
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f0ff; 
  display: flex;
  justify-content: center;
}

#app {
  width: 100%;
  max-width: 1200px; 
  padding: 0 20px; 
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

main section {
  padding: 60px 20px;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}


@media (max-width: 1024px) {
  main section {
    padding: 50px 15px;
  }
}

@media (max-width: 768px) {
  main section {
    padding: 40px 10px;
  }
}

@media (max-width: 480px) {
  main section {
    padding: 30px 10px;
  }
}
</style>
