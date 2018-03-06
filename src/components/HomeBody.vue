<template>
  <div class="wrapper">
    <div class="category">
      <div class="main-category">
        <div v-for="item in mainCategory">
          <img :src="item.url">
          <p>{{item.name}}</p>
        </div>
      </div>
      <div class="other-category">
        <div v-for="i in 10">
          <img src="../assets/logo.png">
          <p>美食</p>
        </div>
      </div>
    </div>

    <div class="recommend">

    </div>

    <div class="likes">

    </div>
  </div>
</template>

<script>
  let imgUrls = []
  for (let i = 0; i < 5; i++) {
    imgUrls.push(require('../assets/t' + String(i) +'.png'))
  }

  let mainCategory = [
    {name: '美食', url: imgUrls[0]},
    {name: '电影/演出', url: imgUrls[1]},
    {name: '酒店/住宿', url: imgUrls[2]},
    {name: '休闲娱乐', url: imgUrls[3]},
    {name: '外卖', url: imgUrls[4]}
  ]

  export default {
    data() {
      return {
        mainCategory: mainCategory
      }
    }
  }
</script>

<style>
  .wrapper {
    background-color: #eee;
  }
  .category {
    border-top: 1px solid #ccc;
    height: 500px;
    background-color: #fff;
  }
  .main-category {
    display: flex;
    height: 200px;
    flex-wrap: wrap;
    border-bottom: 1px solid #ddd;
  }
  .other-category {
    display: flex;
    height: 150px;
    flex-wrap: wrap;
  }
  .main-category div, .other-category div {
    width: 20%;
    height: 100%;
    position: relative;
  }
  .main-category img {
    height: 90px;
    width: 90px;
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%,-50%);
  }
  .main-category p {
    font-size: 26px;
    width: 180px;
    text-align: center;
    color: #666;
    position: absolute;
    top: 64%;
    left: 50%;
    transform: translate(-50%,-50%);
  }
  .other-category img {
    height: 60px;
    width: 60px;
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%,-50%);
  }
  .other-category p {
    position: absolute;
    top: 60%;
    left: 50%;
    transform: translate(-50%,-50%);
    font-size: 26px;
    width: 180px;
    text-align: center;
    color: #666;
  }
  .recommend {
    height: 200px;
    /*border: 1px solid #ddd;*/
    margin: 20px 0;
    background-color: #fff;
  }
  .likes {
    height: 200px;
    background-color: #fff;
  }
</style>
