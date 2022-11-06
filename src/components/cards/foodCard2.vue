<!-- 推荐菜单里面的商品展示卡 -->
<template>
    <n-card class = "foodCardClass2" embedded>
      <template #cover>
        <img :src="{logoUrl}" class = "foodCardImageClass2">
      </template>
      <h3 class = "foodCardName">{{name}}</h3>
      <p class = "foodCardNumber">销量：{{number}}</p>
      <h3 class = "foodCardPrice">￥{{price}}</h3>
    </n-card>
  </template>

<script>
import { defineComponent ,ref } from 'vue'
import { NCarousel,NCard,NButton} from 'naive-ui'
export default defineComponent({
  name: 'foodCard2',
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
.foodCardClass2 {
    width: 300px;
    height: 410px;
    padding-bottom: 0%;
}

.foodCardImageClass2 {
    width: 300px;
    height: 300px;
}

</style>