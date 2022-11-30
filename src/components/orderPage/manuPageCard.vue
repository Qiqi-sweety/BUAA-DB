<!-- userOrderPage的子组件：用于用户进行点菜操作以及展示本店铺的菜品 -->

<!-- TODO:
1.展示本店铺的所有商品，实例化foodCard1，进行展示
2.根据菜单里面的foodCard1中的添加购物车按钮，返回该商品的信息，传给userOrderPage，userOrderPage再将信息传给orderTab中的购物车 -->


<template>
      <n-card 
      style = " height: 95%;
              width: 95%;
              margin: auto;
              margin-top:2%;
              margin-bottom: 50px">
         <!-- 主体部分，分为首页，商品，评价 -->
        <!-- 商品页 -->
    <el-row class = "foodRowClass">
      <el-col :span="6">
        <foodCard1 logoUrl = "" name = "烤黑糖波波牛乳" number = 0 price = 19> </foodCard1>
      
      </el-col>
      <el-col :span="6">
        <foodCard1  logoUrl = "" name = "多肉葡萄" number = 0 price = 28></foodCard1>
        
      </el-col>
      <el-col :span="6"><foodCard1/></el-col>
      <el-col :span="6"><foodCard1/></el-col>
    </el-row>
  </n-card>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NCard , } from 'naive-ui'

  export default defineComponent({
    components: {
      NCard,
    },
  })
  </script>
  <style>

  .foodRowClass {
    margin-left : 50px;
  }

</style>