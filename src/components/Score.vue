<template>
  <div class="score">
      <span>Score: {{wins}}-{{draws}}-{{loses}}</span>
  </div>
</template>

<script>
export default {
  name: "Score",
  props: {
    wins: Number,
    draws: Number,
    loses: Number
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
