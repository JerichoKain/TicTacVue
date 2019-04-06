<template>
  <div class="score">
    <span>{{ wins }} Wins - {{ loses }} Loses - {{ draws }} Draws</span>
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
<style scoped>
span {
  font-size: 2em;
}
</style>
