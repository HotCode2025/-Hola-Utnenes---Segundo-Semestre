<script setup>
import perfil from "../assets/Perfil.png";
import LogosBar from "./LogosBar.vue";
</script>

<template>
  <header>
    <img
      :src="perfil"
      alt="Foto de Cristian Gabriel Moya"
      class="foto-perfil"
    />
    <h1>Cristian Gabriel Moya</h1>
    <p>Técnico en Turismo | Programador en formación | Fotógrafo</p>

    <nav>
      <a href="#sobre-mi">Sobre mí</a>
      <a href="#proyectos">Proyectos</a>
      <a href="#tecnologias">Tecnologías</a>
      <a href="#contacto">Contacto</a>
    </nav>

    <LogosBar />
  </header>
</template>
