<!-- 包含商品信息的店铺卡片 -->
<!-- 用于userMainPage中按照商家搜索的结果展示 -->
<template>
    <n-card hoverable class = "storeCardClass2" embedded>
        <el-row>
            <el-col :span="10">
                <img :src="`/api${store.logo}`" class = "storeCardImageClass2" alt="LOGO">
            </el-col>
            <el-col :span="14">
                <h3 class = "nameClass">
                    {{store.name}}
                </h3>
                <el-row>
                    <el-col :span="12">
                      <el-rate
                          disabled
                          v-model="store.star"
                          class = "rateClass"
                          size="large"/>
                    </el-col>
                    <el-col :span="12">
                        <p class = "numberClass">
                        销量：{{store.sales}}
                        </p>
                    </el-col>
                </el-row>
                
                <n-button type="warning" class = "inButtonClass" size = "large" @click="act_enter">
                进入店铺
              </n-button> 
            
            </el-col>
        </el-row>
<!--        TODO-->
        <el-row >
            <el-col :span="8" v-for="foodItem in items">
                <store-card-food-card :logoUrl="foodItem.image"
                                      :name="foodItem.name"
                                      :price="foodItem.price" />
            </el-col>
        </el-row>
    </n-card>
  </template>

<script>
import { defineComponent } from 'vue'
import { NCarousel,NCard,NButton, NRate} from 'naive-ui'
import storeCardFoodCard from './storeCardFoodCard.vue'
export default defineComponent({
  name: 'storeCard2',
  components: {
    NCarousel,
    NCard,
    NButton,
    NRate,
    storeCardFoodCard,
  },
  props: {
      store:{
        type: Object
      },
      items:{
        type: Array
      },
  },
  methods: {
    act_enter() {
      this.$router.push({
        name: 'userOrderPage',
        query: {store_id: this.store.id}
      })
    }
  }
})
</script>

<style>
.storeCardClass2 {
    width: 550px;
    height: 450px;
    padding-left: 0;
}

.storeCardImageClass2 {
    margin-left: 0;
    width: 200px;
    height: 200px;
   
}

.nameClass {
    font-size: 25px;
    margin-top: 0;
    
}

.numberClass {
    margin-top: 20px;
}

.rateClass {
    
    margin-top: 20px;
}

.inButtonClass {
    margin-left: 180px;
    
}

/*.foodName {*/
/*    margin-top: 0%;*/
/*    margin-left: 10px;*/
/*    margin-bottom:0% ;*/
/*}*/

/*.foodPrice {*/
/*    margin-top: 0%;*/
/*    margin-left: 10px;*/
/*    font-weight: bold;*/
/*    */
/*}*/

</style>
