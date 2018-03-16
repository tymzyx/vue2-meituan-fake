<template>
  <div class="wrapper">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    props: {
      value: String
    }
  }
</script>

<style scoped>
  .wrapper {
    display: flex;
    text-align: center;
  }
</style>
