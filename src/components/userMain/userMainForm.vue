<!-- userMainPage的子组件：包含展示轮播图和猜你喜欢推荐部分 -->

<!-- TODO:根据后端的推荐餐厅list，新建storeCard1的list，将结果进行展示-->


<template>
    <el-form :model="form" class = "userMainFormClass">
      <el-form-item
      style = "width: 1200px;
              height: 550px;
              margin: auto;
              background-color: white;
              border-radius: 10px;">
        <!-- 轮播图 -->
        <n-carousel show-arrow style = "height: 550px;" >
          <img
            class="carousel-img"
            src = "../../assets/food1.jpg"
            alt="暂无图片"
          >

          <img
            class="carousel-img"
            src = "../../assets/food2.jpg"
            alt="暂无图片"
          >

          <!-- <img
            class="carousel-img"
            src = "../../assets/food3.jpg"
          >

          <img
            class="carousel-img"
            src = "../../assets/food4.jpg"
          > -->

        </n-carousel>
      </el-form-item>

      <el-form-item class="recommendListItem">
        <el-form :model="form" style = "width: 100%;">
          <el-form-item
          style = "height: 60px;
                  width: 100%;
                  margin-bottom: 0;">
            <h3 style = "font-size: 30px;
                  margin-top : 25px;
                  margin-left : 3%;">
              猜你喜欢
            </h3>
            <n-tag type="warning" style = "margin: 0 auto 20px;">
              个性推荐
            </n-tag>

          </el-form-item>
          <el-form-item 
          style = "padding-left: 3%;
                  padding-right: 2.5%;
                  padding-top: 10px;">
            <el-row
            style = "width: 100%;
                    margin-bottom: 0;
                    margin-top: 0;">
              <div v-for="(item, index) in stores" :key="index">
                <el-col style = "padding-right: 0;" :span="12">
                  <store-card1
                      :storeLogoUrl="item.logo"
                      :storeName="item.name"
                      :time="'?'"
                      :star="item.star"
                      :number="item.sales"
                  ></store-card1>
                </el-col>
              </div>
            </el-row>

          </el-form-item>
        </el-form> 

          </el-form-item>
        </el-form>
  </template>

<script>
    import storeCard1 from "../cards/storeCard1.vue"
    
    import { defineComponent } from 'vue'
    import { NCarousel,NTag} from 'naive-ui'

    export default defineComponent({
      name: 'userMainForm',
      components: {
        NCarousel,
        storeCard1,
        NTag,
      },
      props: {
        inputKey: {type: String, required: true},
        inputLabel: {type: String, default: "商品"}
      },
      data() {
        return {
          stores: [
              {'id': 123456, 'name': "这是店名", 'address': "这是地址",
                'logo': "", 'info': "这是信息", 'star': 5, 'sales': 321}
          ]
        }
      }
    })
  </script>


  <style>

    .recommendListItem {
        /* border: 2px solid black; */
        width: 1200px;
        background-color: white;
        border-radius: 10px;
        margin: auto;
    }

    .carousel-img {
      height: 550px;
      width: 1200px;
    }
  </style>