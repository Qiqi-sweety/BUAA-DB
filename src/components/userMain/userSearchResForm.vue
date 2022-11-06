<!-- userMainPage的子组件：搜索结果组件 -->

<!-- TODO:根据搜索返回的list，构建展示卡，将结果进行展示
如果是按照店铺搜索，则建立storeCard1；
如果是按照商品搜索，则建立storeCard2； -->

<template>
    <el-form :model="form">
      <el-form-item
      style = "width: 1200px;
              background-color: white;
              border-radius: 10px;
              margin: auto;">

<el-form :model="form" style = "width: 100%;">
      <el-form-item style = "    height: 60px;
        width: 100%;">
            <h3 
            style = "font-size: 30px;
                    margin-top : 10px;
                    margin-left : 3%;">
              搜索结果
            </h3>

            
          </el-form-item>
          <el-form-item style = "padding-left: 3%;padding-right: 2.5%;">
            <el-row style = "width: 100%;">
              <el-col style = "padding-right: 0%;" :span="12">
                <store-card2/>
              </el-col>
              <el-col style = "padding-right: 0%;" :span="12"><store-card2/></el-col>
            </el-row>
            

          </el-form-item>
        </el-form>

      </el-form-item>
    </el-form>
</template>

<script>
  import storeCard2 from "../cards/storeCard2.vue"
  import storeCard1 from "../cards/storeCard1.vue"
  
  export default {
    name: 'userSearchResForm',
    components: {
      storeCard2,
      storeCard1,
    }
  }
</script>
