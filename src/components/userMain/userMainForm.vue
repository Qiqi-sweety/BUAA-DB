<!-- userMainPage的子组件：包含展示轮播图和猜你喜欢推荐部分 -->

<!-- TODO:根据后端的推荐餐厅list，新建storeCard1的list，将结果进行展示-->


<template>
    <el-form class = "userMainFormClass">
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
        <el-form :model="info" style = "width: 100%;">
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
                    padding-top: 10px;"
          >
            <el-row
            style = "width: 100%;
                    margin-bottom: 0;
                    margin-top: 0;">
              <div v-for="(item, index) in info.stores" :key="index">
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
    import { defineComponent, reactive } from 'vue'
    import { NCarousel,NTag} from 'naive-ui'
    import {user_recommend} from "@/api/userMain";



    export default defineComponent({
      name: 'userMainForm',
      components: {
        NCarousel,
        storeCard1,
        NTag,
      },
      setup() {
        const info = reactive({
          stores: [
            {'id': 123456, 'name': "这是店名1", 'address': "这是地址1",
              'logo': "/media/2eecdd44-55ae-42d0-9764-f82b979d59a4.jpg", 'info': "这是信息1", 'star': 5, 'sales': 321},
            {'id': 789012, 'name': "这是店名2", 'address': "这是地址2",
              'logo': "/media/144d6d9c-9157-4010-bd23-594ef753f0ca.jpg", 'info': "这是信息2", 'star': 4, 'sales': 888},
          ],
        })

        user_recommend()
            .then(res => {
              const store_list = res.data.recommended_stores
              console.log(store_list)
              if (res) {
                store_list.forEach(item => {
                  info.stores.push(item)
                })
              }
              console.log(info.stores)
            })
        return {
          info
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