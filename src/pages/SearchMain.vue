<template>
  <div class="sc-container">
    <div class="s-head">
      <i class="fa fa-search search-icon"></i>
      <input class="search" id="search" type="text" placeholder="搜索" v-model="searchValue">
      <span @click="cancel">取消</span>
    </div>

    <div class="body-wrapper-default" v-if="!searchListFlag">
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

    <div class="body-wrapper-list" v-if="searchListFlag">
      <div v-for="i in searchList" class="item"><span><i class="iconfont icon-search" v-if="i.name"></i>{{i.name}}</span></div>
    </div>
  </div>
</template>

<script>
  import {mapState} from 'vuex'

  const _ = require('lodash');

  let fakeHot = ['万里长城', '水立方', 'BEJ48星梦剧院', '奥林匹克公园', '天安门']
  let fakeHistory = ['缘来赫赫小厨麻辣香锅', '金榜园', '黄记煌', '鲜果时刻']

  export default {
    data() {
      return {
        hots: fakeHot,
        histories: fakeHistory,
        searchValue: '',
        searchList: new Array(20),
        searchListFlag: false,  // 是否显示搜索结果条目
      }
    },
    computed: {
      ...mapState(['selectedCity'])
    },
    mounted() {
      document.getElementById('search').focus();
    },
    watch: {
      searchValue() {
        this.getSearchRes();
      }
    },
    methods: {
      getSearchRes: _.debounce(function () {  // 根据输入框内容匹配结果，_.debounce控制判断频率
        let nowValue = this.searchValue;
        for (let i = 0; i < 20; i++) {
          this.$set(this.searchList, i, '');
        }
        if (nowValue === '') {
          this.searchListFlag = false;
          return;
        }

        let _this = this;

        this.$http.get('http://localhost:7766/api/v1/searchPlace', {
          params: {cityName: this.selectedCity, keyword: nowValue}
        }).then(function (res) {
          let result = res.data;
          if (result.code === '0') {
            throw new Error(result.name)
          } else {
            result.forEach((val, index) => {
              _this.$set(_this.searchList, index, val);
            });
            _this.searchListFlag = true;
          }
        }).catch(function (error) {
          console.log('error: ', error);
        });

      }, 500),
      cancel() {
        window.history.back();
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
  .body-wrapper-list {
    width: 100%;
    position: absolute;
    top: 80px;
    bottom: 0;
    border-top: 1px solid #bbb;
    margin-top: 20px;
    text-align: center;
  }
  .item {
    height: 6%;
    width: 90%;
    text-align: left;
    font-size: 28px;
    margin: auto;
    border-bottom: 1px solid #ddd;
    position: relative;
  }
  .item span {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    -webkit-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
  }
  .item i {
    margin-right: 16px;
    font-size: 28px;
  }
</style>
