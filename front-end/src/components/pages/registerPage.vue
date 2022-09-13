<template>
    <div class="registerLayout">
      <el-container>
        <el-header>
  
        </el-header>
        <el-main>
          <div class = "registerClass">
            <storeRegisterCard1/>
            <storeRegisterCard2/>
            <StoreRegisterCard3/>
            <!-- <userRegisterCard/> -->
          </div>
        </el-main>
      </el-container>
    </div>
    
</template>
  
<script>
  import userRegisterCard from '../register/userRegisterCard.vue'
  import storeRegisterCard1 from '../register/storeRegisterCard1.vue'
  import storeRegisterCard2 from '../register/storeRegisterCard2.vue'
  import storeRegisterCard3 from '../register/storeRegisterCard3.vue'

  export default {
    name: 'registerPage',
    components: {
    userRegisterCard,
    storeRegisterCard1,
    storeRegisterCard2,
    storeRegisterCard3,
}
  }
</script>
  
<style>
  .el-header {
    height: 60px;
    background-color: white;
  }
  
  .el-main {
    height: 870px;
  }
  
  .registerClass {
    margin-top: 5%;
  }
  
</style>
  