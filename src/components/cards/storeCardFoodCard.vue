<!-- storeCard2的子组件：显示该店铺包含搜索词的商品卡 -->

<template>
    <img :src="`/api${logoUrl}`"
    style ="width: 150px;
    height: 150px;
    margin-left: 10px;"/>

    <p class = "foodName"> {{name}} </p>
    <p class = "foodPrice"> ￥{{price}} </p>
</template>

<script>
export default{
  props:{
      logoUrl:{
        type:String
      },
      name:{
        type:String
      },
      price:{
        type:Number
      },
    }
}
</script>