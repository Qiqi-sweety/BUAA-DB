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
          >

          <img
            class="carousel-img"
            src = "../../assets/food2.jpg"
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
                  margin-bottom: 0%;">
            <h3 style = "font-size: 30px;
                  margin-top : 25px;
                  margin-left : 3%;">
              猜你喜欢
            </h3>
            <n-tag type="warning" style = "margin-left:20px;
        margin-top:0px;">
              个性推荐
            </n-tag>

          </el-form-item>
          <el-form-item 
          style = "padding-left: 3%;
                  padding-right: 2.5%;
                  padding-top: 10px;">
            <el-row
            style = "width: 100%;
                    margin-bottom: 0%;
                    margin-top: 0%;">
              <el-col :span="12" style = "padding-right: 0%;">
                <store-card1/>
              </el-col>
              <el-col :span="12" style = "padding-right: 0%;">
                <store-card1/>
              </el-col>
            </el-row>
            <el-row
            style = "width: 100%;
                    margin-bottom: 0%;
                    margin-top: 0%;">
              <el-col :span="12" style = "padding-right: 0%;">
                <store-card1/>
              </el-col>
              <el-col  :span="12" style = "padding-right: 0%;"><store-card1/></el-col>
            </el-row>

          </el-form-item>
        </el-form> 

          </el-form-item>
        </el-form>
  </template>

<script>
    import storeCard1 from "../cards/storeCard1.vue"
    
    import { defineComponent ,ref } from 'vue'
    import { NCarousel,NTag} from 'naive-ui'

    export default defineComponent({
      name: 'userMainForm',
      components: {
        NCarousel,
        storeCard1,
        NTag,
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