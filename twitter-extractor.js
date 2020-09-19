console.log("start bot");

var Twit = require('twit');

var config = require('./config');

var T = new Twit(config);

		//SEARCH TWEETS

var params ={
	q: '(wild horses)',
	lang: 'en',
	tweet_mode: 'extended',
 	count: 5
}

T.get('search/tweets', params, gotData)

function gotData(err, data, response) {
	console.log(data);			//# to see list of data parameters
	var tweets = data.statuses;
	for (var i = 0; i < tweets.length; i++){

// console.log(tweets[i].id);
		console.log(tweets[i].full_text);
	}
  }
