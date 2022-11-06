<!-- 可以加入购物车的商品展示卡 -->

<!-- 位于userOrderPage -->

<!-- 需要动态初始化的值:
  1.商品图片
  2.商品名称
  3.销量
  4.价格 -->


<template>
    <n-card class = "foodCardClass1" embedded>
      <template #cover>
        <img :src= "{logoUrl}" class = "foodCardImageClass1">
      </template>
      <h3 class = "foodCardName">{{name}}</h3>
      <p class = "foodCardNumber">销量：{{number}}</p>
      <el-row class = "foodCardRow">
        <el-col :span="12"><h3 class = "foodCardPrice">￥{{price}}</h3></el-col>
        <el-col :span="12">
          <n-button class = "joinButtonClass" type="warning" size = "medium">
            加入购物车
          </n-button>
        </el-col>
      </el-row>
      

    </n-card>
  </template>

<script>
import { defineComponent ,ref } from 'vue'
import { NCarousel,NCard,NButton} from 'naive-ui'

export default defineComponent({
  name: 'foodCard1',
  components: {
    NCarousel,
    NCard,
    NButton,
  },
  props:{
    logoUrl:{
      type:String
    },
    name:{
      type:String
    },
    number:{
      type:Number
    },
    price:{
      type:Number
    }
  },
})
</script>

<style>

.foodCardName {
  margin-top: 0%;
  font-size: 20px;
  margin-bottom: 0%;
}

.foodCardNumber {
  margin-top: 0%;
  margin-bottom: 0%;
}

.joinButtonClass {
  margin-top: 5px;
  margin-left: 20px;
}

.foodCardPrice {
  color: red;
  margin-top: 5px;
  margin-bottom: 0%;
}

.foodCardRow {
  margin-top: 0%;
  margin-bottom: 0%;
}
.foodCardClass1 {
    width: 300px;
    height: 430px;
    padding-bottom: 0%;
}

.foodCardImageClass1 {
    width: 300px;
    height: 300px;
}

</style>