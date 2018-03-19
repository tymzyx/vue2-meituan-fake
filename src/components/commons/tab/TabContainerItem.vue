<template>
  <div v-if="id === $parent.value">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    props: ['id']
  }
</script>

<style>

</style>
