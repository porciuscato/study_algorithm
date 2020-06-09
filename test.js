#! node

var relationship1 = {
  name: "zero",
  friends: ["nero"], //"hero", "xero"],
  logFriends: function () {
    var that = this;
    this.friends.forEach(function (friend) {
      console.log(this);
      console.log(friend);
      console.log(typeof friend);
      //   console.log(that.name, friend);
    });
  },
};

// relationship1.logFriends();

var relationship2 = {
  name: "zero",
  friends: ["nero", "hero", "xero"],
  logFriends: function () {
    console.log(this);
    // console.log(this.friends);
  },
};

relationship2.logFriends();
