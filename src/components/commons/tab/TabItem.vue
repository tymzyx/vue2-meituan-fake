<template>
  <div @click="$parent.$emit('input', id)" class="tab-item-wrapper" :class="{'tab-item-is-selected': $parent.value === id}">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    props: ['id'],
  }
</script>

<style>
  .tab-item-wrapper {
    height: 80px;
    color: #000;
    flex: 1;
    line-height: 80px;
    text-align: center;
    font-size: 28px;
    color: #555;
  }
  .tab-item-is-selected {
    height: 68px !important;
    color: 	#FF7256;
    border-bottom: 2px solid 	#FF7256;
  }
</style>
