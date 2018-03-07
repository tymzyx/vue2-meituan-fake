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
        <div v-for="item in otherCategory">
          <i :class="item.url" :style="{color: item.color}"></i>
          <p>{{item.name}}</p>
        </div>
      </div>
    </div>

    <div class="recommend">
      <div class="recommend-child">
        <!--<div class="card" style="background: url('../assets/home.png')">-->
          <!--<img >-->
        <!--</div>-->
        <div class="card" v-for="i in 2">
          <img src="../assets/hongkong.jpg">
        </div>
      </div>
      <div class="recommend-child">
        <div class="card" v-for="i in 2">
          <img src="../assets/hongkong.jpg">
        </div>
      </div>
    </div>

    <div class="likes">
      <div class="likes-head">
        <span>-猜你喜欢-</span>
      </div>
      <div class="likes-body">
        <div v-for="i in 3" class="likes-item">
          <div class="likes-item-left">
          </div>
          <div class="likes-item-right">
            <h4>麦当劳</h4> <span class="dis">2.8km</span>
            <p>45分钟送达</p>
            <p>起送价¥30|配送费¥6</p> <span class="sales">月售1092</span>
            <div class="label">满50减10</div>
          </div>
        </div>
      </div>
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

  let otherCategory = [
    {name: '打车', url: "iconfont icon-car", color: 'blue'},
    {name: 'KTV', url: "iconfont icon-huatong", color: 'green'},
    {name: '周边游', url: "iconfont icon-gongyuan", color: 'blue'},
    {name: '机票/火车票', url: "iconfont icon-plane", color: 'blue'},
    {name: '跑腿代购', url: "iconfont icon-run", color: 'orange'},
    {name: '健身中心', url: "iconfont icon-dumbbell", color: 'blue'},
    {name: '婚纱摄影', url: "iconfont icon-camera", color: '#FF00FF'},
    {name: '音乐培训', url: "iconfont icon-music", color: 'green'},
    {name: '装修设计', url: "iconfont icon-antdesign", color: 'green'},
    {name: '全部分类', url: "iconfont icon-all", color: 'blue'}
  ]

  export default {
    data() {
      return {
        mainCategory: mainCategory,
        otherCategory: otherCategory
      }
    }
  }
</script>

<style scoped>
  .wrapper {
    background-color: #eee;
    margin-top: 90px;
  }
  .category {
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
  .other-category i {
    font-size: 50px;
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
    height: 500px;
    /*border: 1px solid #ddd;*/
    margin: 20px 0;
    background-color: #fff;
    padding-top: 15px;
  }
  .recommend-child {
    display: flex;
    height: 220px;
    margin: 10px;
  }
  .card {
    height: 100%;
    width: auto;
    background: #ddd;
    margin: 10px;
   }
  .card img {
    width: 100%;
    height: 100%;
  }
  .likes {
    /*height: 200px;*/
    background-color: #fff;
    padding: 0 26px;
    margin-bottom: 100px;
  }
  .likes-head {
    text-align: center;
    padding: 20px 0;
    border-bottom: 1px solid #ddd;
  }
  .likes-item {
    height: 210px;
    padding: 16px 0 24px 0;
    border-bottom: 1px solid #ddd;
  }
  .likes-item-left {
    width: 210px;
    height: 210px;
    background: url("../assets/mdl.jpg");
    background-size: contain;
    float: left;
  }
  .likes-item-right {
    width: 458px;
    float: left;
    padding-left: 30px;
    position: relative;
  }
  .likes-item-right h4 {
    margin: 0 0 10px 0;
    font-size: 35px;
  }
  .likes-item-right p {
    margin: 0 0 10px 0;
    font-size: 28px;
    color: #666;
  }
  .likes-item-right span {
    font-size: 28px;
    color: #666;
  }
  .dis {
    position: absolute;
    top: 2px;
    right: 20px;
  }
  .sales {
    position: absolute;
    bottom: 50px;
    right: 20px;
  }
  .label {
    border: 1px solid #FFAEB9;
    border-radius: 6px;
    background: #FFE4E1;
    font-size: 24px;
    color: red;
    float: left;
    padding: 2px 6px;
  }
</style>
