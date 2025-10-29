<script setup>
import ComponenteEducacion from './components/ComponenteEducacion.vue';
import ComponenteExperiencia from './components/ComponenteExperiencia.vue';
import ComponenteHabilidades from './components/ComponenteHabilidades.vue';
import ComponenteIntereses from './components/ComponenteIntereses.vue';
import ComponenteProyectos from './components/componenteProyectos.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import NavBar from './components/NavBar.vue'
</script>

<template>
  <header>
            <!--        BARRA DE NAVEGACION      -->
                <NavBar />
            <!--        TARJETAS DE PRESENTACION    -->
                <DatosPersonales />
  </header>
  <main>
    <section id="educacion">
        <h2>EDUCACION</h2>
      <ComponenteEducacion />
    </section>
    <section id="experiencia">
        <h2>EXPERIENCIA</h2>
      <ComponenteExperiencia />
    </section>
    <section id="proyectos">
        <h2>PROYECTOS</h2>
      <ComponenteProyectos />
    </section>
    <section id="habilidades">
        <h2>HABILIDADES</h2>
      <ComponenteHabilidades />
    </section>
    <section id="intereses">
        <h2>INTERESES</h2>
      <ComponenteIntereses />
    </section>
  </main>
</template>

<style scoped>

</style>
