<template>
  <div class="wrapper">
    <div class="head-wrapper">
      {{index}}
    </div>
    <div class="body-wrapper">
      <button v-for="city in cities">{{city.name}}</button>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['index', 'cities']
  }
</script>

<style scoped>
  .wrapper {
    margin: 0 0;
  }
  .head-wrapper {
    border-top: 1px solid #cccccc;
    padding-left: 10px;
    height: 60px;
    line-height: 60px;
  }
  .body-wrapper {
    border-top: 1px solid #cccccc;
    border-bottom: 1px solid #cccccc;
  }
  button {
    width: 25%;
    height: 80px;
    text-align: center;
    color: #111111;
    cursor: pointer;
    background: white;
    box-sizing: border-box;
    border: 1px solid #eeeeee;
    border-radius: 4px;
    padding: 6px 13px;
    font-size: 30px;
    outline: none;
  }
</style>
