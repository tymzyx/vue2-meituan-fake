<template>
  <div class="sc-container">
    <div class="s-head">
      <i class="fa fa-search search-icon"></i>
      <input class="search" id="search" type="text" placeholder="搜索" v-model="searchValue">
      <span @click="cancel">取消</span>
    </div>

    <div class="body-wrapper-default">
      <div class="hot">
        <div class="widget">
          <p>热门搜索</p>
        </div>
        <button v-for="item in hots">{{item}}</button>
      </div>
      <div class="history">
        <div class="widget">
          <p>历史搜索</p>
          <i class="fa fa-trash-o trash-icon"></i>
        </div>
        <button v-for="item in histories">{{item}}</button>
      </div>
    </div>

    <div class="body-wrapper-list">
      <div v-for="i in searchList" class="item"><span>{{i}}</span></div>
    </div>
  </div>
</template>

<script>
  let fakeHot = ['万里长城', '水立方', 'BEJ48星梦剧院', '奥林匹克公园', '天安门']
  let fakeHistory = ['缘来赫赫小厨麻辣香锅', '金榜园', '黄记煌', '鲜果时刻']

  let fakeDic = [
    {},
  ]

  export default {
    data() {
      return {
        hots: fakeHot,
        histories: fakeHistory,
        searchValue: '',
        searchList: []
      }
    },
    mounted() {
      document.getElementById('search').focus();
    },
    methods: {
      cancel() {
        this.$router.push('/')
      }
    }
  }
</script>

<style scoped>
  .sc-container {
    height: 100%;
    position: relative;
  }
  .s-head {
    width: 750px;
    height: 80px;
    padding-top: 10px;
    line-height: 80px;
  }
  .s-head span {
    font-size: 28px;
    color: dodgerblue;
  }
  .search-icon {
    position: relative;
    left: 56px;
    z-index: 1;
  }
  .search {
    position: relative;
    left: 0;
    background-color: #eeeeee;
    border: none;
    border-radius: 27px;
    height: 54px;
    padding-left: 54px;
    width: 530px;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    margin-right: 30px;
  }
  .body-wrapper-default p {
    margin-left: 40px;
    font-size: 30px;
    color: #666;
    display: inline;
  }
  .history {
    position: relative;
  }
  .trash-icon {
    position: absolute;
    right: 30px;
    color: #666;
  }
  .widget {
    margin: 30px 0;
  }
  button {
    height: 70px;
    margin-left: 46px;
    margin-bottom: 20px;
    text-align: center;
    color: #111111;
    cursor: pointer;
    background: #eeeeee;
    box-sizing: border-box;
    border: 2px solid #dcdfe6;
    border-radius: 6px;
    padding: 6px 13px;
    font-size: 30px;
    outline: none;
  }
</style>
