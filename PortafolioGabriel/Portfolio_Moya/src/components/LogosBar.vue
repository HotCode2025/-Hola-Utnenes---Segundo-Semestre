<script setup>
import astroTech from "../assets/astrotech-logo.png";
import payunia from "../assets/payunia-logo.png";
import astro from "../assets/astroturismo-logo.png";
</script>

<template>
  <div class="logos-strip">
    <div class="logos-bar">
      <img :src="astroTech" alt="AstroTech Malargüe" />
      <img :src="payunia" alt="Payunia Travel" />
      <img :src="astro" alt="Astroturismo Malargüe" />
    </div>
  </div>
</template>

<style scoped>
/* Franja violeta */
.logos-strip {
  margin-top: 24px;
  padding: 10px 24px;
  background-color: #5b2cff; /* violeta */
}

/* Contenedor interno centrado */
.logos-bar {
  display: flex;
  gap: 24px;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

/* Logos SIN fondo negro, solo con sombra suave */
.logos-bar img {
  height: 40px;
  object-fit: contain;
  background: transparent;       /* importante */
  padding: 0;                    /* nada de “tarjetita” negra */
  border-radius: 6px;
  filter: drop-shadow(0 0 6px rgba(0, 0, 0, 0.6));
}
</style>
