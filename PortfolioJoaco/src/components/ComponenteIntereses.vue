<script setup>
import { ref } from 'vue';

const intereses = ref([
  "Apasionado por el mundo de las computadoras y con ganas de seguir aprendiendo sobre ellas",
  "Amante del mundo de la música, en sus diversos géneros y sintonías",
  "Fuerte interés en el mundo de las inversiones, criptomonedas y el mercado",
  "Amante del deporte en general y de poder compartirlo con más personas",
]);
</script>

<template>
  <div class="intereses-contenedor">
    <ul class="contenedor-lista">
      <li class="item" v-for="(int, index) in intereses" :key="index">
        {{ int }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.intereses-contenedor {
  display: flex;
  position: relative;
  margin: 0 auto;
  max-width: 85%;
  padding: 2rem;
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-lg);
  background: var(--color-background-soft);
  box-shadow: 0 8px 25px rgba(100, 100, 255, 0.1);
}

.contenedor-lista {
  list-style-type: none;
  padding: 0;
  margin: 0;
  width: 100%;
}

.item {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  border-radius: var(--border-radius);
  background: var(--color-background-mute);
  color: var(--color-text);
  font-size: 1.1rem;
  line-height: 1.6;
  border: 1px solid transparent;
  transition: all var(--transition-smooth);
  position: relative;
  overflow: hidden;
}

/* Efecto de brillo en hover */
.item::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(167, 139, 250, 0.3),
    rgba(96, 165, 250, 0.3),
    transparent
  );
  transition: left 0.6s ease;
}

.item:hover {
  transform: translateY(-3px);
  border-color: #a78bfa;
  box-shadow: 0 8px 25px rgba(96, 165, 250, 0.25);
}

.item:hover::before {
  left: 100%;
}

.item:active {
  transform: translateY(-1px);
  transition: transform 0.1s ease;
}

/* Pequeño efecto glitch */
@keyframes glitch {
  0% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(-2px, -2px); }
  60% { transform: translate(2px, 2px); }
  80% { transform: translate(2px, -2px); }
  100% { transform: translate(0); }
}

.item:hover {
  animation: glitch 0.3s ease;
}

.item:last-child {
  margin-bottom: 0;
}

@media (max-width: 768px) {
  .intereses-contenedor {
    max-width: 95%;
    padding: 1rem;
  }

  .item {
    padding: 1rem;
    font-size: 1rem;
  }
}
</style>

