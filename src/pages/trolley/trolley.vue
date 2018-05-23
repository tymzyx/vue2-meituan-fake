<template>
  <div class="trolley-wrapper">
    <my-head text="购物车" />
    <div class="trolley-main">
      <div class="trolley-store">
        <div class="store-info">
          <img src="../../assets/mdl.jpg" width="16" height="16"/>
          <span>来自星星的韩式炸鸡（百旺店）</span>
        </div>
        <div class="goods-info">
          <div class="goods-item">
            <img src="../../assets/mdl.jpg" width="80" height="80"/>
            <div class="info">
              <h4>两人欢乐套餐</h4>
              <span>规格：红甜酱</span>
              <div>
                <span>x1</span>
                <p>¥35</p>
              </div>
            </div>
          </div>
        </div>
        <div class="others"></div>
        <div class="payment"></div>
      </div>
    </div>
  </div>
</template>

<script>
  import MyHead from '../../components/commons/Head'

  export default {
    components: {MyHead}
  }
</script>

<style lang="less">
  .trolley-wrapper {
    padding-top: 112px;
    background: #eee;

    .trolley-main {
      background: #eee;

      .trolley-store {
        margin: 18px 0;
        background: #fff;
        padding: 12px 0 12px 18px;

        .store-info {
          display: flex;
          align-items: center;

          span {
            padding: 0 20px;
            font-size: 28px;
          }
        }

        .goods-item {
          display: flex;
          align-items: center;
          margin: 12px 0;
          background: #eee;

          .info {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            padding: 0 16px;
            height: 140px;

            h4 {
              margin: 0;
              font-size: 30px;
            }
            span {
              font-size: 22px;
              color: #aaa;
            }
            div {
              display: flex;
              justify-content: space-between;
            }
            p {
              margin: 0;
              font-size: 26px;
              font-weight: bold;
            }
          }
        }
      }
    }
  }
</style>
