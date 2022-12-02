<!-- 推荐菜单里面的商品展示卡 -->
<template>
    <n-card class = "foodCardClass2" embedded>
      <template #cover>
        <img :src="`/api${props.item.image}`" class = "foodCardImageClass2">
      </template>
      <h3 class = "foodCardName">{{props.item.name}}</h3>
      <p class = "foodCardNumber">销量：{{props.item.sales}}</p>
      <h3 class = "foodCardPrice">￥{{props.item.price}}</h3>
    </n-card>
</template>

<script setup>
import { NCard} from 'naive-ui'

const props = defineProps({
  item: Object,
  store_id: String,
})
</script>

<style>

.foodCardName {
  margin-top: 0;
  font-size: 20px;
  margin-bottom: 0;
}

.foodCardNumber {
  margin-top: 0;
  margin-bottom: 0;
}

.joinButtonClass {
  margin-top: 5px;
  margin-left: 20px;
}

.foodCardPrice {
  color: red;
  margin-top: 5px;
  margin-bottom: 0;
}

.foodCardRow {
  margin-top: 0;
  margin-bottom: 0;
}
.foodCardClass2 {
    width: 300px;
    height: 410px;
    padding-bottom: 0;
}

.foodCardImageClass2 {
    width: 300px;
    height: 300px;
}

</style>