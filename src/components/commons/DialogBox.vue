<template>
  <div class="dialog-wrapper">
    <div class="dialog-main">
      <div class="dialog-top">
        <span>{{dialogText}}</span>
      </div>
      <div class="dialog-bottom" @click="closeDialog">
        <span>好</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['dialogText'],
    methods: {
      closeDialog() {
        this.$emit('closeDialog');
      }
    }
  }
</script>

<style scoped>
  .dialog-wrapper {
    background: rgba(10, 10, 10, 0.2);
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 101;
  }
  .dialog-main {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 560px;
    height: 200px;
    background: #fff;
    border-radius: 20px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .dialog-top, .dialog-bottom {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
  }
  .dialog-top {
    border-bottom: 1px solid #ddd;
  }
  .dialog-top span {
    font-size: 26px;
    font-weight: bold;
  }
  .dialog-bottom span {
    font-size: 30px;
    font-weight: bold;
    color: #6495ED;
  }
</style>
