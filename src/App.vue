<script setup>
import ComponenteEducacion from './components/ComponenteEducacion.vue';
import ComponenteExperiencia from './components/ComponenteExperiencia.vue';
import ComponenteHabilidades from './components/ComponenteHabilidades.vue';
import ComponenteIntereses from './components/ComponenteIntereses.vue';
import ComponenteProyecto from './components/ComponenteProyecto.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import NavBar from './components/NavBar.vue'
</script>

<template>
    <!--PAGINA PRINCIPAL--> 
  <header id="top">
            <!--        BARRA DE NAVEGACION       -->
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
      <ComponenteProyecto />
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
  <footer>
    <a href="#top"> Inicio </a>
    <p> UTNENES - Cohorte 2025 UTN San Rafael </p>
  </footer>
</template>

<style scoped>
footer{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    font-size:1.3rem;
    color:black;
}
h2{
    width: 100%;
    text-align: center;
    margin: 25px;
}
</style>

<style>
body {
  background-color: #f5f5dc; /* beige clásico */
  min-height: 100vh;
  margin: 0;
}

#app {
  background-color: transparent; /* asegurate de no tapar el fondo */
  min-height: 100vh;
}
h2{
    color:black;
}
</style>