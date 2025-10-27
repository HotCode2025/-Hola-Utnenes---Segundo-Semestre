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
      <ComponenteEducacion />
    </section>
    <section id="experiencia">
      <ComponenteExperiencia />
    </section>
    <section id="proyectos">
      <ComponenteProyectos />
    </section>
    <section id="habilidades">
      <ComponenteHabilidades />
    </section>
    <section id="intereses">
      <ComponenteIntereses />
    </section>
  </main>
</template>

<style scoped>

</style>
