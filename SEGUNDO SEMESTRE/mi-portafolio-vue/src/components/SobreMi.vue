<script setup>
import perfil from '@/assets/imagenes/imagenserena.jpg'
</script>

<template>
  <section id="sobremi" class="sobremi">
    <div class="container-sobremi">
      <h2>Sobre Mí</h2>
      <div class="foto-perfil">
        <img :src="perfil" alt="Foto de Serena Olmedo" />
      </div>
      <p>
        Hola, soy Serena Olmedo, estudiante de la Tecnicatura en
        Programación. Me apasiona el desarrollo web y disfruto creando
        soluciones con HTML, CSS y JavaScript.
      </p>
    </div>
  </section>
</template>

<style scoped>

</style>
