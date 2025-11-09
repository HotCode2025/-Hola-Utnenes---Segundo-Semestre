<script setup>
import FondoLava from './FondoLava.vue';
</script>

<template>
  <div class="intereses-contenedor">
    <FondoLava />
    <div class="contenedor-lista">
      <h2>Mis Intereses</h2>
      <ul>
        <li>Me apasiona la <strong>programación</strong> y todo lo relacionado con la <strong>tecnología</strong>. Disfruto aprender nuevas herramientas y crear cosas útiles.</li>
        <li>Amo la <strong>música</strong>: toco la guitarra y me gusta experimentar con diferentes estilos.</li>
        <li>Me encantan los <strong>videojuegos</strong>, tanto por diversión como por el aspecto técnico detrás de ellos.</li>
        <li>Soy amante de los <strong>deportes</strong> en general. Fui <strong>profesor de Educación Física</strong>, así que siempre disfruto mantenerme activo.</li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.intereses-contenedor {
  position: relative;
  padding: 3rem 2rem;
  border-radius: 10px;
  overflow: hidden;
  background-color: transparent;
}

.contenedor-lista {
  position: relative;
  z-index: 1;
  text-align: center;
  color: var(--color-text-light);
}

.contenedor-lista h2 {
  color: var(--color-accent);
  margin-bottom: 1.5rem;
  font-size: 2rem;
  letter-spacing: 1px;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  max-width: 800px;
}

li {
  font-size: 1.2rem;
  margin: 1.2rem 0;
  line-height: 1.7;
  transition: 0.3s;
}

li:hover {
  color: var(--color-accent);
  transform: scale(1.03);
}
</style>
