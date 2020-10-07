package gobark

import (
	"fmt"
	"github.com/asmcos/requests"
)

type JsonResponse struct {
	Code    int
	data    interface{}
	message string
}

type BarkClient struct {
	Domain  string
	KeyList []string
}

func (client BarkClient) Push(options *PushOptions) {
	failingReceiver := make([]string, 0)

	var actualReceivers []string
	if options.Receivers == nil {
		actualReceivers = client.KeyList
	} else {
		actualReceivers = options.Receivers
	}

	for _, key := range actualReceivers {
		url := client.getRequestUrl(options, client.KeyList[0])
		resp, err := requests.Get(url)
		if err != nil {
			failingReceiver = append(failingReceiver, key)
			continue
		}
		data := JsonResponse{}
		err = resp.Json(&data)
		if err != nil || data.Code != 200 {
			failingReceiver = append(failingReceiver, key)
			continue
		}
	}
}

func (client BarkClient) getRequestUrl(options *PushOptions, key string) string {
	result := fmt.Sprintf("https://%s/%s", client.Domain, key)

	if len(options.Title) != 0 {
		result = result + "/" + options.Title
	}
	result = fmt.Sprintf("%s/%s?automatically_copy=%t", result, options.Content, options.AutomaticallyCopy)

	if len(options.Url) != 0 {
		result = result + "&url=" + options.Url
	}

	if len(options.Sound) != 0 {
		result = result + "&sound=" + options.Sound
	}
	return result
}

type PushOptions struct {
	Content           string
	Title             string
	Url               string
	Receivers         []string
	Sound             string
	AutomaticallyCopy bool
}

func (options *PushOptions) SetTitle(title string) *PushOptions {
	options.Title = title
	return options
}

func (options *PushOptions) SetUrl(url string) *PushOptions {
	options.Url = url
	return options
}

func (options *PushOptions) SetReceivers(receivers []string) *PushOptions {
	options.Receivers = receivers
	return options
}

func (options *PushOptions) SetSound(sound string) *PushOptions {
	options.Sound = sound
	return options
}

func (options *PushOptions) SetAutomaticallyCopy(automaticallyCopy bool) *PushOptions {
	options.AutomaticallyCopy = automaticallyCopy
	return options
}

func NewPushOptions(content string) *PushOptions {
	return &PushOptions{
		Content:           content,
		Title:             "",
		Url:               "",
		Receivers:         nil,
		Sound:             "",
		AutomaticallyCopy: false,
	}
}
