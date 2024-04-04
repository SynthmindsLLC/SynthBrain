[Overview](https://platform.openai.com/overview)[Documentation](https://platform.openai.com/docs)[API reference](https://platform.openai.com/docs/api-reference)

Log in

[Sign up‍](https://platform.openai.com/signup)

SearchK

GETTING STARTED

[Introduction](https://platform.openai.com/docs/api-reference/introduction)[Authentication](https://platform.openai.com/docs/api-reference/authentication)[Making requests](https://platform.openai.com/docs/api-reference/making-requests)[Streaming](https://platform.openai.com/docs/api-reference/streaming)

ENDPOINTS

[Audio](https://platform.openai.com/docs/api-reference/audio)[Chat](https://platform.openai.com/docs/api-reference/chat)[Embeddings](https://platform.openai.com/docs/api-reference/embeddings)[Fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning)[Create fine-tuning job](https://platform.openai.com/docs/api-reference/fine-tuning/create)[List fine-tuning jobs](https://platform.openai.com/docs/api-reference/fine-tuning/list)[List fine-tuning events](https://platform.openai.com/docs/api-reference/fine-tuning/list-events)[List fine-tuning checkpoints](https://platform.openai.com/docs/api-reference/fine-tuning/list-checkpoints)[Retrieve fine-tuning job](https://platform.openai.com/docs/api-reference/fine-tuning/retrieve)[Cancel fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning/cancel)[The fine-tuning job object](https://platform.openai.com/docs/api-reference/fine-tuning/object)[The fine-tuning job event object](https://platform.openai.com/docs/api-reference/fine-tuning/event-object)[The fine-tuning job checkpoint object](https://platform.openai.com/docs/api-reference/fine-tuning/checkpoint-object)[Files](https://platform.openai.com/docs/api-reference/files)[Images](https://platform.openai.com/docs/api-reference/images)[Models](https://platform.openai.com/docs/api-reference/models)[Moderations](https://platform.openai.com/docs/api-reference/moderations)

ASSISTANTS

[Assistants](https://platform.openai.com/docs/api-reference/assistants)[Threads](https://platform.openai.com/docs/api-reference/threads)[Messages](https://platform.openai.com/docs/api-reference/messages)[Runs](https://platform.openai.com/docs/api-reference/runs)[Streaming](https://platform.openai.com/docs/api-reference/assistants-streaming)

LEGACY

[Completions](https://platform.openai.com/docs/api-reference/completions)

[

## Introduction

](https://platform.openai.com/docs/api-reference/introduction)

You can interact with the API through HTTP requests from any language, via our official Python bindings, our official Node.js library, or a [community-maintained library](https://platform.openai.com/docs/libraries/community-libraries).

To install the official Python bindings, run the following command:

```bash
pip install openai
```

To install the official Node.js library, run the following command in your Node.js project directory:

```bash
npm install openai@^4.0.0
```

[

## Authentication

](https://platform.openai.com/docs/api-reference/authentication)

The OpenAI API uses API keys for authentication. Visit your [API Keys](https://platform.openai.com/account/api-keys) page to retrieve the API key you'll use in your requests.

**Remember that your API key is a secret!** Do not share it with others or expose it in any client-side code (browsers, apps). Production requests must be routed through your own backend server where your API key can be securely loaded from an environment variable or key management service.

All API requests should include your API key in an `Authorization` HTTP header as follows:

```bash
Authorization: Bearer OPENAI_API_KEY
```

[

### Organization (optional)

](https://platform.openai.com/docs/api-reference/organization-optional)

For users who belong to multiple organizations, you can pass a header to specify which organization is used for an API request. Usage from these API requests will count as usage for the specified organization.

Example curl command:

```bash
1
2
3
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Organization: YOUR_ORG_ID"
```

Example with the `openai` Python package:

```python
1
2
3
4
5
from openai import OpenAI

client = OpenAI(
  organization='YOUR_ORG_ID',
)
```

Example with the `openai` Node.js package:

```javascript
1
2
3
4
5
import OpenAI from "openai";

const openai = new OpenAI({
  organization: 'YOUR_ORG_ID',
});
```

Organization IDs can be found on your [Organization settings](https://platform.openai.com/account/organization) page.

[

## Making requests

](https://platform.openai.com/docs/api-reference/making-requests)

You can paste the command below into your terminal to run your first API request. Make sure to replace `$OPENAI_API_KEY` with your secret API key.

```bash
1
2
3
4
5
6
7
8
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'
```

This request queries the `gpt-3.5-turbo` model (which under the hood points to a [`gpt-3.5-turbo` model variant](https://platform.openai.com/docs/models/gpt-3-5-turbo)) to complete the text starting with a prompt of "_Say this is a test_". You should get a response back that resembles the following:

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
{
    "id": "chatcmpl-abc123",
    "object": "chat.completion",
    "created": 1677858242,
    "model": "gpt-3.5-turbo-0613",
    "usage": {
        "prompt_tokens": 13,
        "completion_tokens": 7,
        "total_tokens": 20
    },
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "\n\nThis is a test!"
            },
            "logprobs": null,
            "finish_reason": "stop",
            "index": 0
        }
    ]
}
```

Now that you've generated your first chat completion, let's break down the [response object](https://platform.openai.com/docs/api-reference/chat/object). We can see the `finish_reason` is `stop` which means the API returned the full chat completion generated by the model without running into any limits. In the choices list, we only generated a single message but you can set the `n` parameter to generate multiple messages choices.

[

## Streaming

](https://platform.openai.com/docs/api-reference/streaming)

The OpenAI API provides the ability to stream responses back to a client in order to allow partial results for certain requests. To achieve this, we follow the [Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) standard. Our official [Node](https://github.com/openai/openai-node?tab=readme-ov-file#streaming-responses) and [Python](https://github.com/openai/openai-python?tab=readme-ov-file#streaming-responses) libraries include helpers to make parsing these events simpler.

Streaming is supported for both the [Chat Completions API](https://platform.openai.com/docs/api-reference/chat/streaming) and the [Assistants API](https://platform.openai.com/docs/api-reference/runs/createRun). This section focuses on how streaming works for Chat Completions. Learn more about how streaming works in the Assistants API [here](https://platform.openai.com/docs/assistants/overview/step-4-create-a-run).

In Python, a streaming request looks like:

```python
1
2
3
4
5
6
7
8
9
10
11
12
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

In Node / Typescript, a streaming request looks like:

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
    const stream = await openai.chat.completions.create({
        model: "gpt-4",
        messages: [{ role: "user", content: "Say this is a test" }],
        stream: true,
    });
    for await (const chunk of stream) {
        process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
}

main();
```

[

#### Parsing Server-sent events

](https://platform.openai.com/docs/api-reference/parsing-server-sent-events)

Parsing Server-sent events is non-trivial and should be done with caution. Simple strategies like splitting by a new line may result in parsing errors. We recommend using [existing client libraries](https://platform.openai.com/docs/libraries) when possible.

[

## Audio

](https://platform.openai.com/docs/api-reference/audio)

Learn how to turn audio into text or text into audio.

Related guide: [Speech to text](https://platform.openai.com/docs/guides/speech-to-text)

[

## Create speech

](https://platform.openai.com/docs/api-reference/audio/createSpeech)

POST https://api.openai.com/v1/audio/speech

Generates audio from the input text.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createspeech-model)

model

string

Required

One of the available [TTS models](https://platform.openai.com/docs/models/tts): `tts-1` or `tts-1-hd`

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createspeech-input)

input

string

Required

The text to generate audio for. The maximum length is 4096 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createspeech-voice)

voice

string

Required

The voice to use when generating the audio. Supported voices are `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech/voice-options).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createspeech-response_format)

response_format

string

Optional

Defaults to mp3

The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createspeech-speed)

speed

number

Optional

Defaults to 1

The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is the default.

### Returns

The audio file content.

Example request

curl

Select librarycurlpythonnode

```bash
1
2
3
4
5
6
7
8
9
curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy"
  }' \
  --output speech.mp3
```

[

## Create transcription

](https://platform.openai.com/docs/api-reference/audio/createTranscription)

POST https://api.openai.com/v1/audio/transcriptions

Transcribes audio into the input language.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranscription-file)

file

file

Required

The audio file object (not file name) to transcribe, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranscription-model)

model

string

Required

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranscription-language)

language

string

Optional

The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranscription-prompt)

prompt

string

Optional

An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text/prompting) should match the audio language.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranscription-response_format)

response_format

string

Optional

Defaults to json

The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranscription-temperature)

temperature

number

Optional

Defaults to 0

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranscription-timestamp_granularities)

timestamp_granularities[]

array

Optional

Defaults to segment

The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.

### Returns

The [transcription object](https://platform.openai.com/docs/api-reference/audio/json-object) or a [verbose transcription object](https://platform.openai.com/docs/api-reference/audio/verbose-json-object).

Default‍Word timestamps‍Segment timestamps‍

Example request

curl

Select librarycurlpythonnode

```bash
1
2
3
4
5
curl https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@/path/to/file/audio.mp3" \
  -F model="whisper-1"
```

Response

```json
1
2
3
{
  "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that."
}
```

[

## Create translation

](https://platform.openai.com/docs/api-reference/audio/createTranslation)

POST https://api.openai.com/v1/audio/translations

Translates audio into English.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranslation-file)

file

file

Required

The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranslation-model)

model

string

Required

ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranslation-prompt)

prompt

string

Optional

An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text/prompting) should be in English.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranslation-response_format)

response_format

string

Optional

Defaults to json

The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio-createtranslation-temperature)

temperature

number

Optional

Defaults to 0

The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

### Returns

The translated text.

Example request

curl

Select librarycurlpythonnode

```bash
1
2
3
4
5
curl https://api.openai.com/v1/audio/translations \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@/path/to/file/german.m4a" \
  -F model="whisper-1"
```

Response

```json
1
2
3
{
  "text": "Hello, my name is Wolfgang and I come from Germany. Where are you heading today?"
}
```

[

## The transcription object

](https://platform.openai.com/docs/api-reference/audio/json-object)

Represents a transcription response returned by model, based on the provided input.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio/json-object-text)

text

string

The transcribed text.

The transcription object

```JSON
1
2
3
{
  "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that."
}
```

[

## The transcription object

](https://platform.openai.com/docs/api-reference/audio/verbose-json-object)

Represents a verbose json transcription response returned by model, based on the provided input.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio/verbose-json-object-language)

language

string

The language of the input audio.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio/verbose-json-object-duration)

duration

string

The duration of the input audio.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio/verbose-json-object-text)

text

string

The transcribed text.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio/verbose-json-object-words)

words

array

Extracted words and their corresponding timestamps.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#audio/verbose-json-object-segments)

segments

array

Segments of the transcribed text and their corresponding details.

Show properties

The transcription object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
{
  "task": "transcribe",
  "language": "english",
  "duration": 8.470000267028809,
  "text": "The beach was a popular spot on a hot summer day. People were swimming in the ocean, building sandcastles, and playing beach volleyball.",
  "segments": [
    {
      "id": 0,
      "seek": 0,
      "start": 0.0,
      "end": 3.319999933242798,
      "text": " The beach was a popular spot on a hot summer day.",
      "tokens": [
        50364, 440, 7534, 390, 257, 3743, 4008, 322, 257, 2368, 4266, 786, 13, 50530
      ],
      "temperature": 0.0,
      "avg_logprob": -0.2860786020755768,
      "compression_ratio": 1.2363636493682861,
      "no_speech_prob": 0.00985979475080967
    },
    ...
  ]
}
```

[

## Chat

](https://platform.openai.com/docs/api-reference/chat)

Given a list of messages comprising a conversation, the model will return a response.

Related guide: [Chat Completions](https://platform.openai.com/docs/guides/text-generation)

[

## Create chat completion

](https://platform.openai.com/docs/api-reference/chat/create)

POST https://api.openai.com/v1/chat/completions

Creates a model response for the given chat conversation.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-messages)

messages

array

Required

A list of messages comprising the conversation so far. [Example Python code](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models).

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-model)

model

string

Required

ID of the model to use. See the [model endpoint compatibility](https://platform.openai.com/docs/models/model-endpoint-compatibility) table for details on which models work with the Chat API.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-frequency_penalty)

frequency_penalty

number or null

Optional

Defaults to 0

Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

[See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-logit_bias)

logit_bias

map

Optional

Defaults to null

Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-logprobs)

logprobs

boolean or null

Optional

Defaults to false

Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. This option is currently not available on the `gpt-4-vision-preview` model.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-top_logprobs)

top_logprobs

integer or null

Optional

An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-max_tokens)

max_tokens

integer or null

Optional

The maximum number of [tokens](https://platform.openai.com/tokenizer) that can be generated in the chat completion.

The total length of input tokens and generated tokens is limited by the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-n)

n

integer or null

Optional

Defaults to 1

How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-presence_penalty)

presence_penalty

number or null

Optional

Defaults to 0

Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

[See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-response_format)

response_format

object

Optional

An object specifying the format that the model must output. Compatible with [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) and all GPT-3.5 Turbo models newer than `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-seed)

seed

integer or null

Optional

This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-stop)

stop

string / array / null

Optional

Defaults to null

Up to 4 sequences where the API will stop generating further tokens.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-stream)

stream

boolean or null

Optional

Defaults to false

If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

We generally recommend altering this or `top_p` but not both.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-top_p)

top_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or `temperature` but not both.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-tools)

tools

array

Optional

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-tool_choice)

tool_choice

string or object

Optional

Controls which (if any) function is called by the model. `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that function.

`none` is the default when no functions are present. `auto` is the default if functions are present.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-function_call)

function_call

Deprecated

string or object

Optional

Deprecated in favor of `tool_choice`.

Controls which (if any) function is called by the model. `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

`none` is the default when no functions are present. `auto` is the default if functions are present.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat-create-functions)

functions

Deprecated

array

Optional

Deprecated in favor of `tools`.

A list of functions the model may generate JSON inputs for.

Show properties

### Returns

Returns a [chat completion](https://platform.openai.com/docs/api-reference/chat/object) object, or a streamed sequence of [chat completion chunk](https://platform.openai.com/docs/api-reference/chat/streaming) objects if the request is streamed.

Default‍Image input‍Streaming‍Functions‍Logprobs‍

Example request

gpt-3.5-turbo

gpt-3.5-turbo

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "You are a helpful assistant." }],
    model: "gpt-3.5-turbo",
  });

  console.log(completion.choices[0]);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-3.5-turbo-0125",
  "system_fingerprint": "fp_44709d6fcb",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "\n\nHello there, how may I assist you today?",
    },
    "logprobs": null,
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```

[

## The chat completion object

](https://platform.openai.com/docs/api-reference/chat/object)

Represents a chat completion response returned by model, based on the provided input.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/object-id)

id

string

A unique identifier for the chat completion.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/object-choices)

choices

array

A list of chat completion choices. Can be more than one if `n` is greater than 1.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/object-created)

created

integer

The Unix timestamp (in seconds) of when the chat completion was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/object-model)

model

string

The model used for the chat completion.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/object-system_fingerprint)

system_fingerprint

string

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/object-object)

object

string

The object type, which is always `chat.completion`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/object-usage)

usage

object

Usage statistics for the completion request.

Show properties

The chat completion object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-3.5-turbo-0125",
  "system_fingerprint": "fp_44709d6fcb",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "\n\nHello there, how may I assist you today?",
    },
    "logprobs": null,
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```

[

## The chat completion chunk object

](https://platform.openai.com/docs/api-reference/chat/streaming)

Represents a streamed chunk of a chat completion response returned by model, based on the provided input.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/streaming-id)

id

string

A unique identifier for the chat completion. Each chunk has the same ID.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/streaming-choices)

choices

array

A list of chat completion choices. Can be more than one if `n` is greater than 1.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/streaming-created)

created

integer

The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/streaming-model)

model

string

The model to generate the completion.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/streaming-system_fingerprint)

system_fingerprint

string

This fingerprint represents the backend configuration that the model runs with. Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#chat/streaming-object)

object

string

The object type, which is always `chat.completion.chunk`.

The chat completion chunk object

```JSON
1
2
3
4
5
6
7
{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}

{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"content":"Hello"},"logprobs":null,"finish_reason":null}]}

....

{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-3.5-turbo-0125", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{},"logprobs":null,"finish_reason":"stop"}]}
```

[

## Embeddings

](https://platform.openai.com/docs/api-reference/embeddings)

Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.

Related guide: [Embeddings](https://platform.openai.com/docs/guides/embeddings)

[

## Create embeddings

](https://platform.openai.com/docs/api-reference/embeddings/create)

POST https://api.openai.com/v1/embeddings

Creates an embedding vector representing the input text.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#embeddings-create-input)

input

string or array

Required

Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model (8192 tokens for `text-embedding-ada-002`), cannot be an empty string, and any array must be 2048 dimensions or less. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#embeddings-create-model)

model

string

Required

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#embeddings-create-encoding_format)

encoding_format

string

Optional

Defaults to float

The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#embeddings-create-dimensions)

dimensions

integer

Optional

The number of dimensions the resulting output embeddings should have. Only supported in `text-embedding-3` and later models.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#embeddings-create-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

### Returns

A list of [embedding](https://platform.openai.com/docs/api-reference/embeddings/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const embedding = await openai.embeddings.create({
    model: "text-embedding-ada-002",
    input: "The quick brown fox jumped over the lazy dog",
    encoding_format: "float",
  });

  console.log(embedding);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [
        0.0023064255,
        -0.009327292,
        .... (1536 floats total for ada-002)
        -0.0028842222,
      ],
      "index": 0
    }
  ],
  "model": "text-embedding-ada-002",
  "usage": {
    "prompt_tokens": 8,
    "total_tokens": 8
  }
}
```

[

## The embedding object

](https://platform.openai.com/docs/api-reference/embeddings/object)

Represents an embedding vector returned by embedding endpoint.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#embeddings/object-index)

index

integer

The index of the embedding in the list of embeddings.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#embeddings/object-embedding)

embedding

array

The embedding vector, which is a list of floats. The length of vector depends on the model as listed in the [embedding guide](https://platform.openai.com/docs/guides/embeddings).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#embeddings/object-object)

object

string

The object type, which is always "embedding".

The embedding object

```JSON
1
2
3
4
5
6
7
8
9
10
{
  "object": "embedding",
  "embedding": [
    0.0023064255,
    -0.009327292,
    .... (1536 floats total for ada-002)
    -0.0028842222,
  ],
  "index": 0
}
```

[

## Fine-tuning

](https://platform.openai.com/docs/api-reference/fine-tuning)

Manage fine-tuning jobs to tailor a model to your specific training data.

Related guide: [Fine-tune models](https://platform.openai.com/docs/guides/fine-tuning)

[

## Create fine-tuning job

](https://platform.openai.com/docs/api-reference/fine-tuning/create)

POST https://api.openai.com/v1/fine_tuning/jobs

Creates a fine-tuning job which begins the process of creating a new model from a given dataset.

Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-create-model)

model

string

Required

The name of the model to fine-tune. You can select one of the [supported models](https://platform.openai.com/docs/guides/fine-tuning/what-models-can-be-fine-tuned).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-create-training_file)

training_file

string

Required

The ID of an uploaded file that contains training data.

See [upload file](https://platform.openai.com/docs/api-reference/files/upload) for how to upload a file.

Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.

See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning) for more details.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-create-hyperparameters)

hyperparameters

object

Optional

The hyperparameters used for the fine-tuning job.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-create-suffix)

suffix

string or null

Optional

Defaults to null

A string of up to 18 characters that will be added to your fine-tuned model name.

For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-3.5-turbo:openai:custom-model-name:7p4lURel`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-create-validation_file)

validation_file

string or null

Optional

The ID of an uploaded file that contains validation data.

If you provide this file, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in the fine-tuning results file. The same data should not be present in both train and validation files.

Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.

See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning) for more details.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-create-integrations)

integrations

array or null

Optional

A list of integrations to enable for your fine-tuning job.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-create-seed)

seed

integer or null

Optional

The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases. If a seed is not specified, one will be generated for you.

### Returns

A [fine-tuning.job](https://platform.openai.com/docs/api-reference/fine-tuning/object) object.

Default‍Epochs‍Validation file‍W&B Integration‍

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const fineTune = await openai.fineTuning.jobs.create({
    training_file: "file-abc123"
  });

  console.log(fineTune);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
{
  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "gpt-3.5-turbo-0125",
  "created_at": 1614807352,
  "fine_tuned_model": null,
  "organization_id": "org-123",
  "result_files": [],
  "status": "queued",
  "validation_file": null,
  "training_file": "file-abc123",
}
```

[

## List fine-tuning jobs

](https://platform.openai.com/docs/api-reference/fine-tuning/list)

GET https://api.openai.com/v1/fine_tuning/jobs

List your organization's fine-tuning jobs

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-list-after)

after

string

Optional

Identifier for the last job from the previous pagination request.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-list-limit)

limit

integer

Optional

Defaults to 20

Number of fine-tuning jobs to retrieve.

### Returns

A list of paginated [fine-tuning job](https://platform.openai.com/docs/api-reference/fine-tuning/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const list = await openai.fineTuning.jobs.list();

  for await (const fineTune of list) {
    console.log(fineTune);
  }
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
{
  "object": "list",
  "data": [
    {
      "object": "fine_tuning.job.event",
      "id": "ft-event-TjX0lMfOniCZX64t9PUQT5hn",
      "created_at": 1689813489,
      "level": "warn",
      "message": "Fine tuning process stopping due to job cancellation",
      "data": null,
      "type": "message"
    },
    { ... },
    { ... }
  ], "has_more": true
}
```

[

## List fine-tuning events

](https://platform.openai.com/docs/api-reference/fine-tuning/list-events)

GET https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/events

Get status updates for a fine-tuning job.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-list-events-fine_tuning_job_id)

fine_tuning_job_id

string

Required

The ID of the fine-tuning job to get events for.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-list-events-after)

after

string

Optional

Identifier for the last event from the previous pagination request.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-list-events-limit)

limit

integer

Optional

Defaults to 20

Number of events to retrieve.

### Returns

A list of fine-tuning event objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const list = await openai.fineTuning.list_events(id="ftjob-abc123", limit=2);

  for await (const fineTune of list) {
    console.log(fineTune);
  }
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
{
  "object": "list",
  "data": [
    {
      "object": "fine_tuning.job.event",
      "id": "ft-event-ddTJfwuMVpfLXseO0Am0Gqjm",
      "created_at": 1692407401,
      "level": "info",
      "message": "Fine tuning job successfully completed",
      "data": null,
      "type": "message"
    },
    {
      "object": "fine_tuning.job.event",
      "id": "ft-event-tyiGuB72evQncpH87xe505Sv",
      "created_at": 1692407400,
      "level": "info",
      "message": "New fine-tuned model created: ft:gpt-3.5-turbo:openai::7p4lURel",
      "data": null,
      "type": "message"
    }
  ],
  "has_more": true
}
```

[

## List fine-tuning checkpoints

](https://platform.openai.com/docs/api-reference/fine-tuning/list-checkpoints)

GET https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/checkpoints

List checkpoints for a fine-tuning job.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-list-checkpoints-fine_tuning_job_id)

fine_tuning_job_id

string

Required

The ID of the fine-tuning job to get checkpoints for.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-list-checkpoints-after)

after

string

Optional

Identifier for the last checkpoint ID from the previous pagination request.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-list-checkpoints-limit)

limit

integer

Optional

Defaults to 10

Number of checkpoints to retrieve.

### Returns

A list of fine-tuning [checkpoint objects](https://platform.openai.com/docs/api-reference/fine-tuning/checkpoint-object) for a fine-tuning job.

Example request

curl

Select librarycurl

```bash
1
2
curl https://api.openai.com/v1/fine_tuning/jobs/ftjob-abc123/checkpoints \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
{
  "object": "list"
  "data": [
    {
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
      "created_at": 1519129973,
      "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom-suffix:96olL566:ckpt-step-2000",
      "metrics": {
        "full_valid_loss": 0.134,
        "full_valid_mean_token_accuracy": 0.874
      },
      "fine_tuning_job_id": "ftjob-abc123",
      "step_number": 2000,
    },
    {
      "object": "fine_tuning.job.checkpoint",
      "id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
      "created_at": 1519129833,
      "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom-suffix:7q8mpxmy:ckpt-step-1000",
      "metrics": {
        "full_valid_loss": 0.167,
        "full_valid_mean_token_accuracy": 0.781
      },
      "fine_tuning_job_id": "ftjob-abc123",
      "step_number": 1000,
    },
  ],
  "first_id": "ftckpt_zc4Q7MP6XxulcVzj4MZdwsAB",
  "last_id": "ftckpt_enQCFmOTGj3syEpYVhBRLTSy",
  "has_more": true
}
```

[

## Retrieve fine-tuning job

](https://platform.openai.com/docs/api-reference/fine-tuning/retrieve)

GET https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}

Get info about a fine-tuning job.

[Learn more about fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-retrieve-fine_tuning_job_id)

fine_tuning_job_id

string

Required

The ID of the fine-tuning job.

### Returns

The [fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning/object) object with the given ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const fineTune = await openai.fineTuning.jobs.retrieve("ftjob-abc123");

  console.log(fineTune);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
{
  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "davinci-002",
  "created_at": 1692661014,
  "finished_at": 1692661190,
  "fine_tuned_model": "ft:davinci-002:my-org:custom_suffix:7q8mpxmy",
  "organization_id": "org-123",
  "result_files": [
      "file-abc123"
  ],
  "status": "succeeded",
  "validation_file": null,
  "training_file": "file-abc123",
  "hyperparameters": {
      "n_epochs": 4,
      "batch_size": 1,
      "learning_rate_multiplier": 1.0
  },
  "trained_tokens": 5768,
  "integrations": [],
  "seed": 0
}
```

[

## Cancel fine-tuning

](https://platform.openai.com/docs/api-reference/fine-tuning/cancel)

POST https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel

Immediately cancel a fine-tune job.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning-cancel-fine_tuning_job_id)

fine_tuning_job_id

string

Required

The ID of the fine-tuning job to cancel.

### Returns

The cancelled [fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning/object) object.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const fineTune = await openai.fineTuning.jobs.cancel("ftjob-abc123");

  console.log(fineTune);
}
main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
{
  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "gpt-3.5-turbo-0125",
  "created_at": 1689376978,
  "fine_tuned_model": null,
  "organization_id": "org-123",
  "result_files": [],
  "hyperparameters": {
    "n_epochs":  "auto"
  },
  "status": "cancelled",
  "validation_file": "file-abc123",
  "training_file": "file-abc123"
}
```

[

## The fine-tuning job object

](https://platform.openai.com/docs/api-reference/fine-tuning/object)

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-id)

id

string

The object identifier, which can be referenced in the API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the fine-tuning job was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-error)

error

object or null

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-fine_tuned_model)

fine_tuned_model

string or null

The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-finished_at)

finished_at

integer or null

The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-hyperparameters)

hyperparameters

object

The hyperparameters used for the fine-tuning job. See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning) for more details.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-model)

model

string

The base model that is being fine-tuned.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-object)

object

string

The object type, which is always "fine_tuning.job".

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-organization_id)

organization_id

string

The organization that owns the fine-tuning job.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-result_files)

result_files

array

The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-status)

status

string

The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-trained_tokens)

trained_tokens

integer or null

The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-training_file)

training_file

string

The file ID used for training. You can retrieve the training data with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-validation_file)

validation_file

string or null

The file ID used for validation. You can retrieve the validation results with the [Files API](https://platform.openai.com/docs/api-reference/files/retrieve-contents).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-integrations)

integrations

array or null

A list of integrations to enable for this fine-tuning job.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/object-seed)

seed

integer

The seed used for the fine-tuning job.

The fine-tuning job object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
{
  "object": "fine_tuning.job",
  "id": "ftjob-abc123",
  "model": "davinci-002",
  "created_at": 1692661014,
  "finished_at": 1692661190,
  "fine_tuned_model": "ft:davinci-002:my-org:custom_suffix:7q8mpxmy",
  "organization_id": "org-123",
  "result_files": [
      "file-abc123"
  ],
  "status": "succeeded",
  "validation_file": null,
  "training_file": "file-abc123",
  "hyperparameters": {
      "n_epochs": 4,
      "batch_size": 1,
      "learning_rate_multiplier": 1.0
  },
  "trained_tokens": 5768,
  "integrations": [],
  "seed": 0
}
```

[

## The fine-tuning job event object

](https://platform.openai.com/docs/api-reference/fine-tuning/event-object)

Fine-tuning job event object

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/event-object-id)

id

string

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/event-object-created_at)

created_at

integer

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/event-object-level)

level

string

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/event-object-message)

message

string

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/event-object-object)

object

string

The fine-tuning job event object

```JSON
1
2
3
4
5
6
7
{
  "object": "fine_tuning.job.event",
  "id": "ftevent-abc123"
  "created_at": 1677610602,
  "level": "info",
  "message": "Created fine-tuning job"
}
```

[

## The fine-tuning job checkpoint object

](https://platform.openai.com/docs/api-reference/fine-tuning/checkpoint-object)

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/checkpoint-object-id)

id

string

The checkpoint identifier, which can be referenced in the API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/checkpoint-object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the checkpoint was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/checkpoint-object-fine_tuned_model_checkpoint)

fine_tuned_model_checkpoint

string

The name of the fine-tuned checkpoint model that is created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/checkpoint-object-step_number)

step_number

integer

The step number that the checkpoint was created at.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/checkpoint-object-metrics)

metrics

object

Metrics at the step number during the fine-tuning job.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/checkpoint-object-fine_tuning_job_id)

fine_tuning_job_id

string

The name of the fine-tuning job that this checkpoint was created from.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#fine-tuning/checkpoint-object-object)

object

string

The object type, which is always "fine_tuning.job.checkpoint".

The fine-tuning job checkpoint object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
{
  "object": "fine_tuning.job.checkpoint",
  "id": "ftckpt_qtZ5Gyk4BLq1SfLFWp3RtO3P",
  "created_at": 1712211699,
  "fine_tuned_model_checkpoint": "ft:gpt-3.5-turbo-0125:my-org:custom_suffix:9ABel2dg:ckpt-step-88",
  "fine_tuning_job_id": "ftjob-fpbNQ3H1GrMehXRf8cO97xTN",
  "metrics": {
    "step": 88,
    "train_loss": 0.478,
    "train_mean_token_accuracy": 0.924,
    "valid_loss": 10.112,
    "valid_mean_token_accuracy": 0.145,
    "full_valid_loss": 0.567,
    "full_valid_mean_token_accuracy": 0.944
  },
  "step_number": 88
}
```

[

## Files

](https://platform.openai.com/docs/api-reference/files)

Files are used to upload documents that can be used with features like [Assistants](https://platform.openai.com/docs/api-reference/assistants) and [Fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning).

[

## Upload file

](https://platform.openai.com/docs/api-reference/files/create)

POST https://api.openai.com/v1/files

Upload a file that can be used across various endpoints. The size of all the files uploaded by one organization can be up to 100 GB.

The size of individual files can be a maximum of 512 MB or 2 million tokens for Assistants. See the [Assistants Tools guide](https://platform.openai.com/docs/assistants/tools) to learn more about the types of files supported. The Fine-tuning API only supports `.jsonl` files.

Please [contact us](https://help.openai.com/) if you need to increase these storage limits.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files-create-file)

file

file

Required

The File object (not file name) to be uploaded.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files-create-purpose)

purpose

string

Required

The intended purpose of the uploaded file.

Use "fine-tune" for [Fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning) and "assistants" for [Assistants](https://platform.openai.com/docs/api-reference/assistants) and [Messages](https://platform.openai.com/docs/api-reference/messages). This allows us to validate the format of the uploaded file is correct for fine-tuning.

### Returns

The uploaded [File](https://platform.openai.com/docs/api-reference/files/object) object.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const file = await openai.files.create({
    file: fs.createReadStream("mydata.jsonl"),
    purpose: "fine-tune",
  });

  console.log(file);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 120000,
  "created_at": 1677610602,
  "filename": "mydata.jsonl",
  "purpose": "fine-tune",
}
```

[

## List files

](https://platform.openai.com/docs/api-reference/files/list)

GET https://api.openai.com/v1/files

Returns a list of files that belong to the user's organization.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files-list-purpose)

purpose

string

Optional

Only return files with the given purpose.

### Returns

A list of [File](https://platform.openai.com/docs/api-reference/files/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const list = await openai.files.list();

  for await (const file of list) {
    console.log(file);
  }
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
{
  "data": [
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 175,
      "created_at": 1613677385,
      "filename": "salesOverview.pdf",
      "purpose": "assistants",
    },
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 140,
      "created_at": 1613779121,
      "filename": "puppy.jsonl",
      "purpose": "fine-tune",
    }
  ],
  "object": "list"
}
```

[

## Retrieve file

](https://platform.openai.com/docs/api-reference/files/retrieve)

GET https://api.openai.com/v1/files/{file_id}

Returns information about a specific file.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files-retrieve-file_id)

file_id

string

Required

The ID of the file to use for this request.

### Returns

The [File](https://platform.openai.com/docs/api-reference/files/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const file = await openai.files.retrieve("file-abc123");

  console.log(file);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 120000,
  "created_at": 1677610602,
  "filename": "mydata.jsonl",
  "purpose": "fine-tune",
}
```

[

## Delete file

](https://platform.openai.com/docs/api-reference/files/delete)

DELETE https://api.openai.com/v1/files/{file_id}

Delete a file.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files-delete-file_id)

file_id

string

Required

The ID of the file to use for this request.

### Returns

Deletion status.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const file = await openai.files.del("file-abc123");

  console.log(file);
}

main();
```

Response

```json
1
2
3
4
5
{
  "id": "file-abc123",
  "object": "file",
  "deleted": true
}
```

[

## Retrieve file content

](https://platform.openai.com/docs/api-reference/files/retrieve-contents)

GET https://api.openai.com/v1/files/{file_id}/content

Returns the contents of the specified file.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files-retrieve-contents-file_id)

file_id

string

Required

The ID of the file to use for this request.

### Returns

The file content.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const file = await openai.files.retrieveContent("file-abc123");

  console.log(file);
}

main();
```

[

## The file object

](https://platform.openai.com/docs/api-reference/files/object)

The `File` object represents a document that has been uploaded to OpenAI.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files/object-id)

id

string

The file identifier, which can be referenced in the API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files/object-bytes)

bytes

integer

The size of the file, in bytes.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files/object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the file was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files/object-filename)

filename

string

The name of the file.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files/object-object)

object

string

The object type, which is always `file`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files/object-purpose)

purpose

string

The intended purpose of the file. Supported values are `fine-tune`, `fine-tune-results`, `assistants`, and `assistants_output`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files/object-status)

status

Deprecated

string

Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#files/object-status_details)

status_details

Deprecated

string

Deprecated. For details on why a fine-tuning training file failed validation, see the `error` field on `fine_tuning.job`.

The file object

```JSON
1
2
3
4
5
6
7
8
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 120000,
  "created_at": 1677610602,
  "filename": "salesOverview.pdf",
  "purpose": "assistants",
}
```

[

## Images

](https://platform.openai.com/docs/api-reference/images)

Given a prompt and/or an input image, the model will generate a new image.

Related guide: [Image generation](https://platform.openai.com/docs/guides/images)

[

## Create image

](https://platform.openai.com/docs/api-reference/images/create)

POST https://api.openai.com/v1/images/generations

Creates an image given a prompt.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-create-prompt)

prompt

string

Required

A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2` and 4000 characters for `dall-e-3`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-create-model)

model

string

Optional

Defaults to dall-e-2

The model to use for image generation.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-create-n)

n

integer or null

Optional

Defaults to 1

The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-create-quality)

quality

string

Optional

Defaults to standard

The quality of the image that will be generated. `hd` creates images with finer details and greater consistency across the image. This param is only supported for `dall-e-3`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-create-response_format)

response_format

string or null

Optional

Defaults to url

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-create-size)

size

string or null

Optional

Defaults to 1024x1024

The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-create-style)

style

string or null

Optional

Defaults to vivid

The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for `dall-e-3`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-create-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

### Returns

Returns a list of [image](https://platform.openai.com/docs/api-reference/images/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const image = await openai.images.generate({ model: "dall-e-3", prompt: "A cute baby sea otter" });

  console.log(image.data);
}
main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
{
  "created": 1589478378,
  "data": [
    {
      "url": "https://..."
    },
    {
      "url": "https://..."
    }
  ]
}
```

[

## Create image edit

](https://platform.openai.com/docs/api-reference/images/createEdit)

POST https://api.openai.com/v1/images/edits

Creates an edited or extended image given an original image and a prompt.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createedit-image)

image

file

Required

The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createedit-prompt)

prompt

string

Required

A text description of the desired image(s). The maximum length is 1000 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createedit-mask)

mask

file

Optional

An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where `image` should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createedit-model)

model

string

Optional

Defaults to dall-e-2

The model to use for image generation. Only `dall-e-2` is supported at this time.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createedit-n)

n

integer or null

Optional

Defaults to 1

The number of images to generate. Must be between 1 and 10.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createedit-size)

size

string or null

Optional

Defaults to 1024x1024

The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createedit-response_format)

response_format

string or null

Optional

Defaults to url

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createedit-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

### Returns

Returns a list of [image](https://platform.openai.com/docs/api-reference/images/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const image = await openai.images.edit({
    image: fs.createReadStream("otter.png"),
    mask: fs.createReadStream("mask.png"),
    prompt: "A cute baby sea otter wearing a beret",
  });

  console.log(image.data);
}
main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
{
  "created": 1589478378,
  "data": [
    {
      "url": "https://..."
    },
    {
      "url": "https://..."
    }
  ]
}
```

[

## Create image variation

](https://platform.openai.com/docs/api-reference/images/createVariation)

POST https://api.openai.com/v1/images/variations

Creates a variation of a given image.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createvariation-image)

image

file

Required

The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createvariation-model)

model

string

Optional

Defaults to dall-e-2

The model to use for image generation. Only `dall-e-2` is supported at this time.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createvariation-n)

n

integer or null

Optional

Defaults to 1

The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createvariation-response_format)

response_format

string or null

Optional

Defaults to url

The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createvariation-size)

size

string or null

Optional

Defaults to 1024x1024

The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images-createvariation-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

### Returns

Returns a list of [image](https://platform.openai.com/docs/api-reference/images/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const image = await openai.images.createVariation({
    image: fs.createReadStream("otter.png"),
  });

  console.log(image.data);
}
main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
{
  "created": 1589478378,
  "data": [
    {
      "url": "https://..."
    },
    {
      "url": "https://..."
    }
  ]
}
```

[

## The image object

](https://platform.openai.com/docs/api-reference/images/object)

Represents the url or the content of an image generated by the OpenAI API.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images/object-b64_json)

b64_json

string

The base64-encoded JSON of the generated image, if `response_format` is `b64_json`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images/object-url)

url

string

The URL of the generated image, if `response_format` is `url` (default).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#images/object-revised_prompt)

revised_prompt

string

The prompt that was used to generate the image, if there was any revision to the prompt.

The image object

```JSON
1
2
3
4
{
  "url": "...",
  "revised_prompt": "..."
}
```

[

## Models

](https://platform.openai.com/docs/api-reference/models)

List and describe the various models available in the API. You can refer to the [Models](https://platform.openai.com/docs/models) documentation to understand what models are available and the differences between them.

[

## List models

](https://platform.openai.com/docs/api-reference/models/list)

GET https://api.openai.com/v1/models

Lists the currently available models, and provides basic information about each one such as the owner and availability.

### Returns

A list of [model](https://platform.openai.com/docs/api-reference/models/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const list = await openai.models.list();

  for await (const model of list) {
    console.log(model);
  }
}
main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
{
  "object": "list",
  "data": [
    {
      "id": "model-id-0",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner"
    },
    {
      "id": "model-id-1",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner",
    },
    {
      "id": "model-id-2",
      "object": "model",
      "created": 1686935002,
      "owned_by": "openai"
    },
  ],
  "object": "list"
}
```

[

## Retrieve model

](https://platform.openai.com/docs/api-reference/models/retrieve)

GET https://api.openai.com/v1/models/{model}

Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#models-retrieve-model)

model

string

Required

The ID of the model to use for this request

### Returns

The [model](https://platform.openai.com/docs/api-reference/models/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const model = await openai.models.retrieve("gpt-3.5-turbo");

  console.log(model);
}

main();
```

Response

gpt-3.5-turbo-instruct

gpt-3.5-turbo-instruct

```json
1
2
3
4
5
6
{
  "id": "gpt-3.5-turbo-instruct",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
}
```

[

## Delete a fine-tuned model

](https://platform.openai.com/docs/api-reference/models/delete)

DELETE https://api.openai.com/v1/models/{model}

Delete a fine-tuned model. You must have the Owner role in your organization to delete a model.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#models-delete-model)

model

string

Required

The model to delete

### Returns

Deletion status.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const model = await openai.models.del("ft:gpt-3.5-turbo:acemeco:suffix:abc123");

  console.log(model);
}
main();
```

Response

```json
1
2
3
4
5
{
  "id": "ft:gpt-3.5-turbo:acemeco:suffix:abc123",
  "object": "model",
  "deleted": true
}
```

[

## The model object

](https://platform.openai.com/docs/api-reference/models/object)

Describes an OpenAI model offering that can be used with the API.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#models/object-id)

id

string

The model identifier, which can be referenced in the API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#models/object-created)

created

integer

The Unix timestamp (in seconds) when the model was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#models/object-object)

object

string

The object type, which is always "model".

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#models/object-owned_by)

owned_by

string

The organization that owns the model.

The model object

gpt-3.5-turbo-instruct

```JSON
1
2
3
4
5
6
{
  "id": "davinci",
  "object": "model",
  "created": 1686935002,
  "owned_by": "openai"
}
```

[

## Moderations

](https://platform.openai.com/docs/api-reference/moderations)

Given some input text, outputs if the model classifies it as potentially harmful across several categories.

Related guide: [Moderations](https://platform.openai.com/docs/guides/moderation)

[

## Create moderation

](https://platform.openai.com/docs/api-reference/moderations/create)

POST https://api.openai.com/v1/moderations

Classifies if text is potentially harmful.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#moderations-create-input)

input

string or array

Required

The input text to classify

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#moderations-create-model)

model

string

Optional

Defaults to text-moderation-latest

Two content moderations models are available: `text-moderation-stable` and `text-moderation-latest`.

The default is `text-moderation-latest` which will be automatically upgraded over time. This ensures you are always using our most accurate model. If you use `text-moderation-stable`, we will provide advanced notice before updating the model. Accuracy of `text-moderation-stable` may be slightly lower than for `text-moderation-latest`.

### Returns

A [moderation](https://platform.openai.com/docs/api-reference/moderations/object) object.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const moderation = await openai.moderations.create({ input: "I want to kill them." });

  console.log(moderation);
}
main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
{
  "id": "modr-XXXXX",
  "model": "text-moderation-005",
  "results": [
    {
      "flagged": true,
      "categories": {
        "sexual": false,
        "hate": false,
        "harassment": false,
        "self-harm": false,
        "sexual/minors": false,
        "hate/threatening": false,
        "violence/graphic": false,
        "self-harm/intent": false,
        "self-harm/instructions": false,
        "harassment/threatening": true,
        "violence": true,
      },
      "category_scores": {
        "sexual": 1.2282071e-06,
        "hate": 0.010696256,
        "harassment": 0.29842457,
        "self-harm": 1.5236925e-08,
        "sexual/minors": 5.7246268e-08,
        "hate/threatening": 0.0060676364,
        "violence/graphic": 4.435014e-06,
        "self-harm/intent": 8.098441e-10,
        "self-harm/instructions": 2.8498655e-11,
        "harassment/threatening": 0.63055265,
        "violence": 0.99011886,
      }
    }
  ]
}
```

[

## The moderation object

](https://platform.openai.com/docs/api-reference/moderations/object)

Represents if a given text input is potentially harmful.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#moderations/object-id)

id

string

The unique identifier for the moderation request.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#moderations/object-model)

model

string

The model used to generate the moderation results.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#moderations/object-results)

results

array

A list of moderation objects.

Show properties

The moderation object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
{
  "id": "modr-XXXXX",
  "model": "text-moderation-005",
  "results": [
    {
      "flagged": true,
      "categories": {
        "sexual": false,
        "hate": false,
        "harassment": false,
        "self-harm": false,
        "sexual/minors": false,
        "hate/threatening": false,
        "violence/graphic": false,
        "self-harm/intent": false,
        "self-harm/instructions": false,
        "harassment/threatening": true,
        "violence": true,
      },
      "category_scores": {
        "sexual": 1.2282071e-06,
        "hate": 0.010696256,
        "harassment": 0.29842457,
        "self-harm": 1.5236925e-08,
        "sexual/minors": 5.7246268e-08,
        "hate/threatening": 0.0060676364,
        "violence/graphic": 4.435014e-06,
        "self-harm/intent": 8.098441e-10,
        "self-harm/instructions": 2.8498655e-11,
        "harassment/threatening": 0.63055265,
        "violence": 0.99011886,
      }
    }
  ]
}
```

[

## Assistants

Beta



](https://platform.openai.com/docs/api-reference/assistants)

Build assistants that can call models and use tools to perform tasks.

[Get started with the Assistants API](https://platform.openai.com/docs/assistants)

[

## Create assistant

Beta



](https://platform.openai.com/docs/api-reference/assistants/createAssistant)

POST https://api.openai.com/v1/assistants

Create an assistant with a model and instructions.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistant-model)

model

Required

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistant-name)

name

string or null

Optional

The name of the assistant. The maximum length is 256 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistant-description)

description

string or null

Optional

The description of the assistant. The maximum length is 512 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistant-instructions)

instructions

string or null

Optional

The system instructions that the assistant uses. The maximum length is 32768 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistant-tools)

tools

array

Optional

Defaults to []

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistant-file_ids)

file_ids

array

Optional

Defaults to []

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistant-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

An [assistant](https://platform.openai.com/docs/api-reference/assistants/object) object.

Code Interpreter‍Files‍

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const myAssistant = await openai.beta.assistants.create({
    instructions:
      "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    name: "Math Tutor",
    tools: [{ type: "code_interpreter" }],
    model: "gpt-4",
  });

  console.log(myAssistant);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1698984975,
  "name": "Math Tutor",
  "description": null,
  "model": "gpt-4",
  "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "file_ids": [],
  "metadata": {}
}
```

[

## Create assistant file

Beta



](https://platform.openai.com/docs/api-reference/assistants/createAssistantFile)

POST https://api.openai.com/v1/assistants/{assistant_id}/files

Create an assistant file by attaching a [File](https://platform.openai.com/docs/api-reference/files) to an [assistant](https://platform.openai.com/docs/api-reference/assistants).

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistantfile-assistant_id)

assistant_id

string

Required

The ID of the assistant for which to create a File.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-createassistantfile-file_id)

file_id

string

Required

A [File](https://platform.openai.com/docs/api-reference/files) ID (with `purpose="assistants"`) that the assistant should use. Useful for tools like `retrieval` and `code_interpreter` that can access files.

### Returns

An [assistant file](https://platform.openai.com/docs/api-reference/assistants/file-object) object.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const myAssistantFile = await openai.beta.assistants.files.create(
    "asst_abc123",
    {
      file_id: "file-abc123"
    }
  );
  console.log(myAssistantFile);
}

main();
```

Response

```json
1
2
3
4
5
6
{
  "id": "file-abc123",
  "object": "assistant.file",
  "created_at": 1699055364,
  "assistant_id": "asst_abc123"
}
```

[

## List assistants

Beta



](https://platform.openai.com/docs/api-reference/assistants/listAssistants)

GET https://api.openai.com/v1/assistants

Returns a list of assistants.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistants-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistants-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistants-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistants-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

### Returns

A list of [assistant](https://platform.openai.com/docs/api-reference/assistants/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const myAssistants = await openai.beta.assistants.list({
    order: "desc",
    limit: "20",
  });

  console.log(myAssistants.data);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{
  "object": "list",
  "data": [
    {
      "id": "asst_abc123",
      "object": "assistant",
      "created_at": 1698982736,
      "name": "Coding Tutor",
      "description": null,
      "model": "gpt-4",
      "instructions": "You are a helpful assistant designed to make me better at coding!",
      "tools": [],
      "file_ids": [],
      "metadata": {}
    },
    {
      "id": "asst_abc456",
      "object": "assistant",
      "created_at": 1698982718,
      "name": "My Assistant",
      "description": null,
      "model": "gpt-4",
      "instructions": "You are a helpful assistant designed to make me better at coding!",
      "tools": [],
      "file_ids": [],
      "metadata": {}
    },
    {
      "id": "asst_abc789",
      "object": "assistant",
      "created_at": 1698982643,
      "name": null,
      "description": null,
      "model": "gpt-4",
      "instructions": null,
      "tools": [],
      "file_ids": [],
      "metadata": {}
    }
  ],
  "first_id": "asst_abc123",
  "last_id": "asst_abc789",
  "has_more": false
}
```

[

## List assistant files

Beta



](https://platform.openai.com/docs/api-reference/assistants/listAssistantFiles)

GET https://api.openai.com/v1/assistants/{assistant_id}/files

Returns a list of assistant files.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistantfiles-assistant_id)

assistant_id

string

Required

The ID of the assistant the file belongs to.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistantfiles-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistantfiles-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistantfiles-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-listassistantfiles-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

### Returns

A list of [assistant file](https://platform.openai.com/docs/api-reference/assistants/file-object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const assistantFiles = await openai.beta.assistants.files.list(
    "asst_abc123"
  );
  console.log(assistantFiles);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
{
  "object": "list",
  "data": [
    {
      "id": "file-abc123",
      "object": "assistant.file",
      "created_at": 1699060412,
      "assistant_id": "asst_abc123"
    },
    {
      "id": "file-abc456",
      "object": "assistant.file",
      "created_at": 1699060412,
      "assistant_id": "asst_abc123"
    }
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc456",
  "has_more": false
}
```

[

## Retrieve assistant

Beta



](https://platform.openai.com/docs/api-reference/assistants/getAssistant)

GET https://api.openai.com/v1/assistants/{assistant_id}

Retrieves an assistant.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-getassistant-assistant_id)

assistant_id

string

Required

The ID of the assistant to retrieve.

### Returns

The [assistant](https://platform.openai.com/docs/api-reference/assistants/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const myAssistant = await openai.beta.assistants.retrieve(
    "asst_abc123"
  );

  console.log(myAssistant);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1699009709,
  "name": "HR Helper",
  "description": null,
  "model": "gpt-4",
  "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies.",
  "tools": [
    {
      "type": "retrieval"
    }
  ],
  "file_ids": [
    "file-abc123"
  ],
  "metadata": {}
}
```

[

## Retrieve assistant file

Beta



](https://platform.openai.com/docs/api-reference/assistants/getAssistantFile)

GET https://api.openai.com/v1/assistants/{assistant_id}/files/{file_id}

Retrieves an AssistantFile.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-getassistantfile-assistant_id)

assistant_id

string

Required

The ID of the assistant who the file belongs to.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-getassistantfile-file_id)

file_id

string

Required

The ID of the file we're getting.

### Returns

The [assistant file](https://platform.openai.com/docs/api-reference/assistants/file-object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const myAssistantFile = await openai.beta.assistants.files.retrieve(
    "asst_abc123",
    "file-abc123"
  );
  console.log(myAssistantFile);
}

main();
```

Response

```json
1
2
3
4
5
6
{
  "id": "file-abc123",
  "object": "assistant.file",
  "created_at": 1699055364,
  "assistant_id": "asst_abc123"
}
```

[

## Modify assistant

Beta



](https://platform.openai.com/docs/api-reference/assistants/modifyAssistant)

POST https://api.openai.com/v1/assistants/{assistant_id}

Modifies an assistant.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-modifyassistant-assistant_id)

assistant_id

string

Required

The ID of the assistant to modify.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-modifyassistant-model)

model

Optional

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-modifyassistant-name)

name

string or null

Optional

The name of the assistant. The maximum length is 256 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-modifyassistant-description)

description

string or null

Optional

The description of the assistant. The maximum length is 512 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-modifyassistant-instructions)

instructions

string or null

Optional

The system instructions that the assistant uses. The maximum length is 32768 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-modifyassistant-tools)

tools

array

Optional

Defaults to []

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-modifyassistant-file_ids)

file_ids

array

Optional

Defaults to []

A list of [File](https://platform.openai.com/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order. If a file was previously attached to the list but does not show up in the list, it will be deleted from the assistant.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-modifyassistant-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [assistant](https://platform.openai.com/docs/api-reference/assistants/object) object.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const myUpdatedAssistant = await openai.beta.assistants.update(
    "asst_abc123",
    {
      instructions:
        "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
      name: "HR Helper",
      tools: [{ type: "retrieval" }],
      model: "gpt-4",
      file_ids: [
        "file-abc123",
        "file-abc456",
      ],
    }
  );

  console.log(myUpdatedAssistant);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1699009709,
  "name": "HR Helper",
  "description": null,
  "model": "gpt-4",
  "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
  "tools": [
    {
      "type": "retrieval"
    }
  ],
  "file_ids": [
    "file-abc123",
    "file-abc456"
  ],
  "metadata": {}
}
```

[

## Delete assistant

Beta



](https://platform.openai.com/docs/api-reference/assistants/deleteAssistant)

DELETE https://api.openai.com/v1/assistants/{assistant_id}

Delete an assistant.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-deleteassistant-assistant_id)

assistant_id

string

Required

The ID of the assistant to delete.

### Returns

Deletion status

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const response = await openai.beta.assistants.del("asst_abc123");

  console.log(response);
}
main();
```

Response

```json
1
2
3
4
5
{
  "id": "asst_abc123",
  "object": "assistant.deleted",
  "deleted": true
}
```

[

## Delete assistant file

Beta



](https://platform.openai.com/docs/api-reference/assistants/deleteAssistantFile)

DELETE https://api.openai.com/v1/assistants/{assistant_id}/files/{file_id}

Delete an assistant file.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-deleteassistantfile-assistant_id)

assistant_id

string

Required

The ID of the assistant that the file belongs to.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-deleteassistantfile-file_id)

file_id

string

Required

The ID of the file to delete.

### Returns

Deletion status

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const deletedAssistantFile = await openai.beta.assistants.files.del(
    "asst_abc123",
    "file-abc123"
  );
  console.log(deletedAssistantFile);
}

main();
```

Response

```json
1
2
3
4
5
{
  id: "file-abc123",
  object: "assistant.file.deleted",
  deleted: true
}
```

[

## The assistant object

Beta



](https://platform.openai.com/docs/api-reference/assistants/object)

Represents an `assistant` that can call the model and use tools.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-object)

object

string

The object type, which is always `assistant`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the assistant was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-name)

name

string or null

The name of the assistant. The maximum length is 256 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-description)

description

string or null

The description of the assistant. The maximum length is 512 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-model)

model

string

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-instructions)

instructions

string or null

The system instructions that the assistant uses. The maximum length is 32768 characters.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-tools)

tools

array

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-file_ids)

file_ids

array

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The assistant object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1698984975,
  "name": "Math Tutor",
  "description": null,
  "model": "gpt-4",
  "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "file_ids": [],
  "metadata": {}
}
```

[

## The assistant file object

Beta



](https://platform.openai.com/docs/api-reference/assistants/file-object)

A list of [Files](https://platform.openai.com/docs/api-reference/files) attached to an `assistant`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/file-object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/file-object-object)

object

string

The object type, which is always `assistant.file`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/file-object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the assistant file was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants/file-object-assistant_id)

assistant_id

string

The assistant ID that the file is attached to.

The assistant file object

```JSON
1
2
3
4
5
6
{
  "id": "file-abc123",
  "object": "assistant.file",
  "created_at": 1699055364,
  "assistant_id": "asst_abc123"
}
```

[

## Threads

Beta



](https://platform.openai.com/docs/api-reference/threads)

Create threads that assistants can interact with.

Related guide: [Assistants](https://platform.openai.com/docs/assistants/overview)

[

## Create thread

Beta



](https://platform.openai.com/docs/api-reference/threads/createThread)

POST https://api.openai.com/v1/threads

Create a thread.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads-createthread-messages)

messages

array

Optional

A list of [messages](https://platform.openai.com/docs/api-reference/messages) to start the thread with.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads-createthread-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

A [thread](https://platform.openai.com/docs/api-reference/threads) object.

Empty‍Messages‍

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const emptyThread = await openai.beta.threads.create();

  console.log(emptyThread);
}

main();
```

Response

```json
1
2
3
4
5
6
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699012949,
  "metadata": {}
}
```

[

## Retrieve thread

Beta



](https://platform.openai.com/docs/api-reference/threads/getThread)

GET https://api.openai.com/v1/threads/{thread_id}

Retrieves a thread.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads-getthread-thread_id)

thread_id

string

Required

The ID of the thread to retrieve.

### Returns

The [thread](https://platform.openai.com/docs/api-reference/threads/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const myThread = await openai.beta.threads.retrieve(
    "thread_abc123"
  );

  console.log(myThread);
}

main();
```

Response

```json
1
2
3
4
5
6
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699014083,
  "metadata": {}
}
```

[

## Modify thread

Beta



](https://platform.openai.com/docs/api-reference/threads/modifyThread)

POST https://api.openai.com/v1/threads/{thread_id}

Modifies a thread.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads-modifythread-thread_id)

thread_id

string

Required

The ID of the thread to modify. Only the `metadata` can be modified.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads-modifythread-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [thread](https://platform.openai.com/docs/api-reference/threads/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const updatedThread = await openai.beta.threads.update(
    "thread_abc123",
    {
      metadata: { modified: "true", user: "abc123" },
    }
  );

  console.log(updatedThread);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699014083,
  "metadata": {
    "modified": "true",
    "user": "abc123"
  }
}
```

[

## Delete thread

Beta



](https://platform.openai.com/docs/api-reference/threads/deleteThread)

DELETE https://api.openai.com/v1/threads/{thread_id}

Delete a thread.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads-deletethread-thread_id)

thread_id

string

Required

The ID of the thread to delete.

### Returns

Deletion status

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const response = await openai.beta.threads.del("thread_abc123");

  console.log(response);
}
main();
```

Response

```json
1
2
3
4
5
{
  "id": "thread_abc123",
  "object": "thread.deleted",
  "deleted": true
}
```

[

## The thread object

Beta



](https://platform.openai.com/docs/api-reference/threads/object)

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads/object-object)

object

string

The object type, which is always `thread`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads/object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the thread was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#threads/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The thread object

```JSON
1
2
3
4
5
6
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1698107661,
  "metadata": {}
}
```

[

## Messages

Beta



](https://platform.openai.com/docs/api-reference/messages)

Create messages within threads

Related guide: [Assistants](https://platform.openai.com/docs/assistants/overview)

[

## Create message

Beta



](https://platform.openai.com/docs/api-reference/messages/createMessage)

POST https://api.openai.com/v1/threads/{thread_id}/messages

Create a message.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-createmessage-thread_id)

thread_id

string

Required

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) to create a message for.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-createmessage-role)

role

string

Required

The role of the entity that is creating the message. Allowed values include:

- `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
- `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-createmessage-content)

content

string

Required

The content of the message.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-createmessage-file_ids)

file_ids

array

Optional

Defaults to []

A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the message should use. There can be a maximum of 10 files attached to a message. Useful for tools like `retrieval` and `code_interpreter` that can access and use files.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-createmessage-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

A [message](https://platform.openai.com/docs/api-reference/messages/object) object.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const threadMessages = await openai.beta.threads.messages.create(
    "thread_abc123",
    { role: "user", content: "How does AI work? Explain it in simple terms." }
  );

  console.log(threadMessages);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1699017614,
  "thread_id": "thread_abc123",
  "role": "user",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "How does AI work? Explain it in simple terms.",
        "annotations": []
      }
    }
  ],
  "file_ids": [],
  "assistant_id": null,
  "run_id": null,
  "metadata": {}
}
```

[

## List messages

Beta



](https://platform.openai.com/docs/api-reference/messages/listMessages)

GET https://api.openai.com/v1/threads/{thread_id}/messages

Returns a list of messages for a given thread.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessages-thread_id)

thread_id

string

Required

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) the messages belong to.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessages-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessages-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessages-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessages-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessages-run_id)

run_id

string

Optional

Filter messages by the run ID that generated them.

### Returns

A list of [message](https://platform.openai.com/docs/api-reference/messages) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const threadMessages = await openai.beta.threads.messages.list(
    "thread_abc123"
  );

  console.log(threadMessages.data);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
{
  "object": "list",
  "data": [
    {
      "id": "msg_abc123",
      "object": "thread.message",
      "created_at": 1699016383,
      "thread_id": "thread_abc123",
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "How does AI work? Explain it in simple terms.",
            "annotations": []
          }
        }
      ],
      "file_ids": [],
      "assistant_id": null,
      "run_id": null,
      "metadata": {}
    },
    {
      "id": "msg_abc456",
      "object": "thread.message",
      "created_at": 1699016383,
      "thread_id": "thread_abc123",
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": {
            "value": "Hello, what is AI?",
            "annotations": []
          }
        }
      ],
      "file_ids": [
        "file-abc123"
      ],
      "assistant_id": null,
      "run_id": null,
      "metadata": {}
    }
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc456",
  "has_more": false
}
```

[

## List message files

Beta



](https://platform.openai.com/docs/api-reference/messages/listMessageFiles)

GET https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}/files

Returns a list of message files.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessagefiles-thread_id)

thread_id

string

Required

The ID of the thread that the message and files belong to.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessagefiles-message_id)

message_id

string

Required

The ID of the message that the files belongs to.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessagefiles-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessagefiles-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessagefiles-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-listmessagefiles-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

### Returns

A list of [message file](https://platform.openai.com/docs/api-reference/messages/file-object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const messageFiles = await openai.beta.threads.messages.files.list(
    "thread_abc123",
    "msg_abc123"
  );
  console.log(messageFiles);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
{
  "object": "list",
  "data": [
    {
      "id": "file-abc123",
      "object": "thread.message.file",
      "created_at": 1699061776,
      "message_id": "msg_abc123"
    },
    {
      "id": "file-abc123",
      "object": "thread.message.file",
      "created_at": 1699061776,
      "message_id": "msg_abc123"
    }
  ],
  "first_id": "file-abc123",
  "last_id": "file-abc123",
  "has_more": false
}
```

[

## Retrieve message

Beta



](https://platform.openai.com/docs/api-reference/messages/getMessage)

GET https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}

Retrieve a message.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-getmessage-thread_id)

thread_id

string

Required

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) to which this message belongs.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-getmessage-message_id)

message_id

string

Required

The ID of the message to retrieve.

### Returns

The [message](https://platform.openai.com/docs/api-reference/threads/messages/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const message = await openai.beta.threads.messages.retrieve(
    "thread_abc123",
    "msg_abc123"
  );

  console.log(message);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1699017614,
  "thread_id": "thread_abc123",
  "role": "user",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "How does AI work? Explain it in simple terms.",
        "annotations": []
      }
    }
  ],
  "file_ids": [],
  "assistant_id": null,
  "run_id": null,
  "metadata": {}
}
```

[

## Retrieve message file

Beta



](https://platform.openai.com/docs/api-reference/messages/getMessageFile)

GET https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}/files/{file_id}

Retrieves a message file.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-getmessagefile-thread_id)

thread_id

string

Required

The ID of the thread to which the message and File belong.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-getmessagefile-message_id)

message_id

string

Required

The ID of the message the file belongs to.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-getmessagefile-file_id)

file_id

string

Required

The ID of the file being retrieved.

### Returns

The [message file](https://platform.openai.com/docs/api-reference/messages/file-object) object.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const messageFile = await openai.beta.threads.messages.files.retrieve(
    "thread_abc123",
    "msg_abc123",
    "file-abc123"
  );
  console.log(messageFile);
}

main();
```

Response

```json
1
2
3
4
5
6
{
  "id": "file-abc123",
  "object": "thread.message.file",
  "created_at": 1699061776,
  "message_id": "msg_abc123"
}
```

[

## Modify message

Beta



](https://platform.openai.com/docs/api-reference/messages/modifyMessage)

POST https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}

Modifies a message.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-modifymessage-thread_id)

thread_id

string

Required

The ID of the thread to which this message belongs.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-modifymessage-message_id)

message_id

string

Required

The ID of the message to modify.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages-modifymessage-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [message](https://platform.openai.com/docs/api-reference/threads/messages/object) object.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const message = await openai.beta.threads.messages.update(
    "thread_abc123",
    "msg_abc123",
    {
      metadata: {
        modified: "true",
        user: "abc123",
      },
    }
  }'
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1699017614,
  "thread_id": "thread_abc123",
  "role": "user",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "How does AI work? Explain it in simple terms.",
        "annotations": []
      }
    }
  ],
  "file_ids": [],
  "assistant_id": null,
  "run_id": null,
  "metadata": {
    "modified": "true",
    "user": "abc123"
  }
}
```

[

## The message object

Beta



](https://platform.openai.com/docs/api-reference/messages/object)

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-object)

object

string

The object type, which is always `thread.message`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the message was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-thread_id)

thread_id

string

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-status)

status

string

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-incomplete_details)

incomplete_details

object or null

On an incomplete message, details about why the message is incomplete.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-completed_at)

completed_at

integer or null

The Unix timestamp (in seconds) for when the message was completed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-incomplete_at)

incomplete_at

integer or null

The Unix timestamp (in seconds) for when the message was marked as incomplete.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-role)

role

string

The entity that produced the message. One of `user` or `assistant`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-content)

content

array

The content of the message in array of text and/or images.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-assistant_id)

assistant_id

string or null

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-run_id)

run_id

string or null

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-file_ids)

file_ids

array

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs that the assistant should use. Useful for tools like retrieval and code_interpreter that can access files. A maximum of 10 files can be attached to a message.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

The message object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1698983503,
  "thread_id": "thread_abc123",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "Hi! How can I help you today?",
        "annotations": []
      }
    }
  ],
  "file_ids": [],
  "assistant_id": "asst_abc123",
  "run_id": "run_abc123",
  "metadata": {}
}
```

[

## The message file object

Beta



](https://platform.openai.com/docs/api-reference/messages/file-object)

A list of files attached to a `message`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/file-object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/file-object-object)

object

string

The object type, which is always `thread.message.file`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/file-object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the message file was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#messages/file-object-message_id)

message_id

string

The ID of the [message](https://platform.openai.com/docs/api-reference/messages) that the [File](https://platform.openai.com/docs/api-reference/files) is attached to.

The message file object

```JSON
1
2
3
4
5
6
7
{
  "id": "file-abc123",
  "object": "thread.message.file",
  "created_at": 1698107661,
  "message_id": "message_QLoItBbqwyAJEzlTy4y9kOMM",
  "file_id": "file-abc123"
}
```

[

## Runs

Beta



](https://platform.openai.com/docs/api-reference/runs)

Represents an execution run on a thread.

Related guide: [Assistants](https://platform.openai.com/docs/assistants/overview)

[

## Create run

Beta



](https://platform.openai.com/docs/api-reference/runs/createRun)

POST https://api.openai.com/v1/threads/{thread_id}/runs

Create a run.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-thread_id)

thread_id

string

Required

The ID of the thread to run.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-assistant_id)

assistant_id

string

Required

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) to use to execute this run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-model)

model

string or null

Optional

The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-instructions)

instructions

string or null

Optional

Overrides the [instructions](https://platform.openai.com/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-additional_instructions)

additional_instructions

string or null

Optional

Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-additional_messages)

additional_messages

array or null

Optional

Adds additional messages to the thread before creating the run.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-tools)

tools

array or null

Optional

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createrun-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

### Returns

A [run](https://platform.openai.com/docs/api-reference/runs/object) object.

Default‍Streaming‍Streaming with Functions‍

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const run = await openai.beta.threads.runs.create(
    "thread_abc123",
    { assistant_id: "asst_abc123" }
  );

  console.log(run);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699063290,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "queued",
  "started_at": 1699063290,
  "expires_at": null,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": 1699063291,
  "last_error": null,
  "model": "gpt-4",
  "instructions": null,
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "file_ids": [
    "file-abc123",
    "file-abc456"
  ],
  "metadata": {},
  "usage": null,
  "temperature": 1
}
```

[

## Create thread and run

Beta



](https://platform.openai.com/docs/api-reference/runs/createThreadAndRun)

POST https://api.openai.com/v1/threads/runs

Create a thread and run it in one request.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createthreadandrun-assistant_id)

assistant_id

string

Required

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) to use to execute this run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createthreadandrun-thread)

thread

object

Optional

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createthreadandrun-model)

model

string or null

Optional

The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createthreadandrun-instructions)

instructions

string or null

Optional

Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createthreadandrun-tools)

tools

array or null

Optional

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createthreadandrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createthreadandrun-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-createthreadandrun-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

### Returns

A [run](https://platform.openai.com/docs/api-reference/runs/object) object.

Default‍Streaming‍Streaming with Functions‍

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const run = await openai.beta.threads.createAndRun({
    assistant_id: "asst_abc123",
    thread: {
      messages: [
        { role: "user", content: "Explain deep learning to a 5 year old." },
      ],
    },
  });

  console.log(run);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076792,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "queued",
  "started_at": null,
  "expires_at": 1699077392,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4",
  "instructions": "You are a helpful assistant.",
  "tools": [],
  "file_ids": [],
  "metadata": {},
  "usage": null,
  "temperature": 1
}
```

[

## List runs

Beta



](https://platform.openai.com/docs/api-reference/runs/listRuns)

GET https://api.openai.com/v1/threads/{thread_id}/runs

Returns a list of runs belonging to a thread.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listruns-thread_id)

thread_id

string

Required

The ID of the thread the run belongs to.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listruns-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listruns-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listruns-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listruns-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

### Returns

A list of [run](https://platform.openai.com/docs/api-reference/runs/object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const runs = await openai.beta.threads.runs.list(
    "thread_abc123"
  );

  console.log(runs);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
{
  "object": "list",
  "data": [
    {
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699075072,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699075072,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699075073,
      "last_error": null,
      "model": "gpt-3.5-turbo",
      "instructions": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [
        "file-abc123",
        "file-abc456"
      ],
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1
    },
    {
      "id": "run_abc456",
      "object": "thread.run",
      "created_at": 1699063290,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699063290,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699063291,
      "last_error": null,
      "model": "gpt-3.5-turbo",
      "instructions": null,
      "tools": [
        {
          "type": "code_interpreter"
        }
      ],
      "file_ids": [
        "file-abc123",
        "file-abc456"
      ],
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      },
      "temperature": 1
    }
  ],
  "first_id": "run_abc123",
  "last_id": "run_abc456",
  "has_more": false
}
```

[

## List run steps

Beta



](https://platform.openai.com/docs/api-reference/runs/listRunSteps)

GET https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/steps

Returns a list of run steps belonging to a run.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listrunsteps-thread_id)

thread_id

string

Required

The ID of the thread the run and run steps belong to.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listrunsteps-run_id)

run_id

string

Required

The ID of the run the run steps belong to.

### Query parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listrunsteps-limit)

limit

integer

Optional

Defaults to 20

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listrunsteps-order)

order

string

Optional

Defaults to desc

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listrunsteps-after)

after

string

Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-listrunsteps-before)

before

string

Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

### Returns

A list of [run step](https://platform.openai.com/docs/api-reference/runs/step-object) objects.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const runStep = await openai.beta.threads.runs.steps.list(
    "thread_abc123",
    "run_abc123"
  );
  console.log(runStep);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
{
  "object": "list",
  "data": [
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "created_at": 1699063291,
      "run_id": "run_abc123",
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "type": "message_creation",
      "status": "completed",
      "cancelled_at": null,
      "completed_at": 1699063291,
      "expired_at": null,
      "failed_at": null,
      "last_error": null,
      "step_details": {
        "type": "message_creation",
        "message_creation": {
          "message_id": "msg_abc123"
        }
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      }
    }
  ],
  "first_id": "step_abc123",
  "last_id": "step_abc456",
  "has_more": false
}
```

[

## Retrieve run

Beta



](https://platform.openai.com/docs/api-reference/runs/getRun)

GET https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}

Retrieves a run.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-getrun-thread_id)

thread_id

string

Required

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-getrun-run_id)

run_id

string

Required

The ID of the run to retrieve.

### Returns

The [run](https://platform.openai.com/docs/api-reference/runs/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const run = await openai.beta.threads.runs.retrieve(
    "thread_abc123",
    "run_abc123"
  );

  console.log(run);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699075072,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "completed",
  "started_at": 1699075072,
  "expires_at": null,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": 1699075073,
  "last_error": null,
  "model": "gpt-3.5-turbo",
  "instructions": null,
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "file_ids": [
    "file-abc123",
    "file-abc456"
  ],
  "metadata": {},
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 456,
    "total_tokens": 579
  },
  "temperature": 1
}
```

[

## Retrieve run step

Beta



](https://platform.openai.com/docs/api-reference/runs/getRunStep)

GET https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/steps/{step_id}

Retrieves a run step.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-getrunstep-thread_id)

thread_id

string

Required

The ID of the thread to which the run and run step belongs.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-getrunstep-run_id)

run_id

string

Required

The ID of the run to which the run step belongs.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-getrunstep-step_id)

step_id

string

Required

The ID of the run step to retrieve.

### Returns

The [run step](https://platform.openai.com/docs/api-reference/runs/step-object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
import OpenAI from "openai";
const openai = new OpenAI();

async function main() {
  const runStep = await openai.beta.threads.runs.steps.retrieve(
    "thread_abc123",
    "run_abc123",
    "step_abc123"
  );
  console.log(runStep);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
{
  "id": "step_abc123",
  "object": "thread.run.step",
  "created_at": 1699063291,
  "run_id": "run_abc123",
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "type": "message_creation",
  "status": "completed",
  "cancelled_at": null,
  "completed_at": 1699063291,
  "expired_at": null,
  "failed_at": null,
  "last_error": null,
  "step_details": {
    "type": "message_creation",
    "message_creation": {
      "message_id": "msg_abc123"
    }
  },
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 456,
    "total_tokens": 579
  }
}
```

[

## Modify run

Beta



](https://platform.openai.com/docs/api-reference/runs/modifyRun)

POST https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}

Modifies a run.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-modifyrun-thread_id)

thread_id

string

Required

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-modifyrun-run_id)

run_id

string

Required

The ID of the run to modify.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-modifyrun-metadata)

metadata

map

Optional

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

### Returns

The modified [run](https://platform.openai.com/docs/api-reference/runs/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const run = await openai.beta.threads.runs.update(
    "thread_abc123",
    "run_abc123",
    {
      metadata: {
        user_id: "user_abc123",
      },
    }
  );

  console.log(run);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699075072,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "completed",
  "started_at": 1699075072,
  "expires_at": null,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": 1699075073,
  "last_error": null,
  "model": "gpt-3.5-turbo",
  "instructions": null,
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "file_ids": [
    "file-abc123",
    "file-abc456"
  ],
  "metadata": {
    "user_id": "user_abc123"
  },
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 456,
    "total_tokens": 579
  },
  "temperature": 1
}
```

[

## Submit tool outputs to run

Beta



](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs)

POST https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs

When a run has the `status: "requires_action"` and `required_action.type` is `submit_tool_outputs`, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-submittooloutputs-thread_id)

thread_id

string

Required

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) to which this run belongs.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-submittooloutputs-run_id)

run_id

string

Required

The ID of the run that requires the tool output submission.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-submittooloutputs-tool_outputs)

tool_outputs

array

Required

A list of tools for which the outputs are being submitted.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-submittooloutputs-stream)

stream

boolean or null

Optional

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

### Returns

The modified [run](https://platform.openai.com/docs/api-reference/runs/object) object matching the specified ID.

Default‍Streaming‍

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const run = await openai.beta.threads.runs.submitToolOutputs(
    "thread_123",
    "run_123",
    {
      tool_outputs: [
        {
          tool_call_id: "call_001",
          output: "70 degrees and sunny.",
        },
      ],
    }
  );

  console.log(run);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
{
  "id": "run_123",
  "object": "thread.run",
  "created_at": 1699075592,
  "assistant_id": "asst_123",
  "thread_id": "thread_123",
  "status": "queued",
  "started_at": 1699075592,
  "expires_at": 1699076192,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4",
  "instructions": null,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "file_ids": [],
  "metadata": {},
  "usage": null,
  "temperature": 1
}
```

[

## Cancel a run

Beta



](https://platform.openai.com/docs/api-reference/runs/cancelRun)

POST https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/cancel

Cancels a run that is `in_progress`.

### Path parameters

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-cancelrun-thread_id)

thread_id

string

Required

The ID of the thread to which this run belongs.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs-cancelrun-run_id)

run_id

string

Required

The ID of the run to cancel.

### Returns

The modified [run](https://platform.openai.com/docs/api-reference/runs/object) object matching the specified ID.

Example request

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const run = await openai.beta.threads.runs.cancel(
    "thread_abc123",
    "run_abc123"
  );

  console.log(run);
}

main();
```

Response

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076126,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "cancelling",
  "started_at": 1699076126,
  "expires_at": 1699076726,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4",
  "instructions": "You summarize books.",
  "tools": [
    {
      "type": "retrieval"
    }
  ],
  "file_ids": [],
  "metadata": {},
  "usage": null,
  "temperature": 1
}
```

[

## The run object

Beta



](https://platform.openai.com/docs/api-reference/runs/object)

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-id)

id

string

The identifier, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-object)

object

string

The object type, which is always `thread.run`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the run was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-thread_id)

thread_id

string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-assistant_id)

assistant_id

string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-status)

status

string

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, or `expired`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-required_action)

required_action

object or null

Details on the action required to continue the run. Will be `null` if no action is required.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-last_error)

last_error

object or null

The last error associated with this run. Will be `null` if there are no errors.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-expires_at)

expires_at

integer or null

The Unix timestamp (in seconds) for when the run will expire.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-started_at)

started_at

integer or null

The Unix timestamp (in seconds) for when the run was started.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-cancelled_at)

cancelled_at

integer or null

The Unix timestamp (in seconds) for when the run was cancelled.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-failed_at)

failed_at

integer or null

The Unix timestamp (in seconds) for when the run failed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-completed_at)

completed_at

integer or null

The Unix timestamp (in seconds) for when the run was completed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-model)

model

string

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-instructions)

instructions

string

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-tools)

tools

array

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-file_ids)

file_ids

array

The list of [File](https://platform.openai.com/docs/api-reference/files) IDs the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-usage)

usage

object or null

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/object-temperature)

temperature

number or null

The sampling temperature used for this run. If not set, defaults to 1.

The run object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
{
  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1698107661,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "completed",
  "started_at": 1699073476,
  "expires_at": null,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": 1699073498,
  "last_error": null,
  "model": "gpt-4",
  "instructions": null,
  "tools": [{"type": "retrieval"}, {"type": "code_interpreter"}],
  "file_ids": [],
  "metadata": {},
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 456,
    "total_tokens": 579
  },
  "temperature": 1
}
```

[

## The run step object

Beta



](https://platform.openai.com/docs/api-reference/runs/step-object)

Represents a step in execution of a run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-id)

id

string

The identifier of the run step, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-object)

object

string

The object type, which is always `thread.run.step`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-created_at)

created_at

integer

The Unix timestamp (in seconds) for when the run step was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-assistant_id)

assistant_id

string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-thread_id)

thread_id

string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-run_id)

run_id

string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-type)

type

string

The type of run step, which can be either `message_creation` or `tool_calls`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-status)

status

string

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-step_details)

step_details

object

The details of the run step.

Show possible types

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-last_error)

last_error

object or null

The last error associated with this run step. Will be `null` if there are no errors.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-expired_at)

expired_at

integer or null

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-cancelled_at)

cancelled_at

integer or null

The Unix timestamp (in seconds) for when the run step was cancelled.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-failed_at)

failed_at

integer or null

The Unix timestamp (in seconds) for when the run step failed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-completed_at)

completed_at

integer or null

The Unix timestamp (in seconds) for when the run step completed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-metadata)

metadata

map

Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#runs/step-object-usage)

usage

object or null

Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.

Show properties

The run step object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
{
  "id": "step_abc123",
  "object": "thread.run.step",
  "created_at": 1699063291,
  "run_id": "run_abc123",
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "type": "message_creation",
  "status": "completed",
  "cancelled_at": null,
  "completed_at": 1699063291,
  "expired_at": null,
  "failed_at": null,
  "last_error": null,
  "step_details": {
    "type": "message_creation",
    "message_creation": {
      "message_id": "msg_abc123"
    }
  },
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 456,
    "total_tokens": 579
  }
}
```

[

## Streaming

Beta



](https://platform.openai.com/docs/api-reference/assistants-streaming)

Stream the result of executing a Run or resuming a Run after submitting tool outputs.

You can stream events from the [Create Thread and Run](https://platform.openai.com/docs/api-reference/runs/createThreadAndRun), [Create Run](https://platform.openai.com/docs/api-reference/runs/createRun), and [Submit Tool Outputs](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoints by passing `"stream": true`. The response will be a [Server-Sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events) stream.

Our Node and Python SDKs provide helpful utilities to make streaming easy. Reference the [Assistants API quickstart](https://platform.openai.com/docs/assistants/overview) to learn more.

[

## The message delta object

Beta



](https://platform.openai.com/docs/api-reference/assistants-streaming/message-delta-object)

Represents a message delta i.e. any changed fields on a message during streaming.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/message-delta-object-id)

id

string

The identifier of the message, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/message-delta-object-object)

object

string

The object type, which is always `thread.message.delta`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/message-delta-object-delta)

delta

object

The delta containing the fields that have changed on the Message.

Show properties

The message delta object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
{
  "id": "msg_123",
  "object": "thread.message.delta",
  "delta": {
    "content": [
      {
        "index": 0,
        "type": "text",
        "text": { "value": "Hello", "annotations": [] }
      }
    ]
  }
}
```

[

## The run step delta object

Beta



](https://platform.openai.com/docs/api-reference/assistants-streaming/run-step-delta-object)

Represents a run step delta i.e. any changed fields on a run step during streaming.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/run-step-delta-object-id)

id

string

The identifier of the run step, which can be referenced in API endpoints.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/run-step-delta-object-object)

object

string

The object type, which is always `thread.run.step.delta`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/run-step-delta-object-delta)

delta

object

The delta containing the fields that have changed on the run step.

Show properties

The run step delta object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
{
  "id": "step_123",
  "object": "thread.run.step.delta",
  "delta": {
    "step_details": {
      "type": "tool_calls",
      "tool_calls": [
        {
          "index": 0,
          "id": "call_123",
          "type": "code_interpreter",
          "code_interpreter": { "input": "", "outputs": [] }
        }
      ]
    }
  }
}
```

[

## Assistant stream events

Beta



](https://platform.openai.com/docs/api-reference/assistants-streaming/events)

Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

```json
event: thread.created
data: {"id": "thread_123", "object": "thread", ...}
```

We emit events whenever a new object is created, transitions to a new state, or is being streamed in parts (deltas). For example, we emit `thread.run.created` when a new run is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses to create a message during a run, we emit a `thread.message.created event`, a `thread.message.in_progress` event, many `thread.message.delta` events, and finally a `thread.message.completed` event.

We may add additional events over time, so we recommend handling unknown events gracefully in your code. See the [Assistants API quickstart](https://platform.openai.com/docs/assistants/overview) to learn how to integrate the Assistants API with streaming.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-created)

thread.created

`data` is a [thread](https://platform.openai.com/docs/api-reference/threads/object)

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-created)

thread.run.created

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-queued)

thread.run.queued

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-in_progress)

thread.run.in_progress

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-requires_action)

thread.run.requires_action

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-completed)

thread.run.completed

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-failed)

thread.run.failed

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-cancelling)

thread.run.cancelling

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-cancelled)

thread.run.cancelled

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-expired)

thread.run.expired

`data` is a [run](https://platform.openai.com/docs/api-reference/runs/object)

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-step-created)

thread.run.step.created

`data` is a [run step](https://platform.openai.com/docs/api-reference/runs/step-object)

Occurs when a [run step](https://platform.openai.com/docs/api-reference/runs/step-object) is created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-step-in_progress)

thread.run.step.in_progress

`data` is a [run step](https://platform.openai.com/docs/api-reference/runs/step-object)

Occurs when a [run step](https://platform.openai.com/docs/api-reference/runs/step-object) moves to an `in_progress` state.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-step-delta)

thread.run.step.delta

`data` is a [run step delta](https://platform.openai.com/docs/api-reference/assistants-streaming/run-step-delta-object)

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/runs/step-object) are being streamed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-step-completed)

thread.run.step.completed

`data` is a [run step](https://platform.openai.com/docs/api-reference/runs/step-object)

Occurs when a [run step](https://platform.openai.com/docs/api-reference/runs/step-object) is completed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-step-failed)

thread.run.step.failed

`data` is a [run step](https://platform.openai.com/docs/api-reference/runs/step-object)

Occurs when a [run step](https://platform.openai.com/docs/api-reference/runs/step-object) fails.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-step-cancelled)

thread.run.step.cancelled

`data` is a [run step](https://platform.openai.com/docs/api-reference/runs/step-object)

Occurs when a [run step](https://platform.openai.com/docs/api-reference/runs/step-object) is cancelled.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-run-step-expired)

thread.run.step.expired

`data` is a [run step](https://platform.openai.com/docs/api-reference/runs/step-object)

Occurs when a [run step](https://platform.openai.com/docs/api-reference/runs/step-object) expires.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-message-created)

thread.message.created

`data` is a [message](https://platform.openai.com/docs/api-reference/messages/object)

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-message-in_progress)

thread.message.in_progress

`data` is a [message](https://platform.openai.com/docs/api-reference/messages/object)

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-message-delta)

thread.message.delta

`data` is a [message delta](https://platform.openai.com/docs/api-reference/assistants-streaming/message-delta-object)

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-message-completed)

thread.message.completed

`data` is a [message](https://platform.openai.com/docs/api-reference/messages/object)

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-thread-message-incomplete)

thread.message.incomplete

`data` is a [message](https://platform.openai.com/docs/api-reference/messages/object)

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-error)

error

`data` is an [error](https://platform.openai.com/docs/guides/error-codes/api-errors)

Occurs when an [error](https://platform.openai.com/docs/guides/error-codes/api-errors) occurs. This can happen due to an internal server error or a timeout.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#assistants-streaming/events-done)

done

`data` is `[DONE]`

Occurs when a stream ends.

[

## Completions

Legacy



](https://platform.openai.com/docs/api-reference/completions)

Given a prompt, the model will return one or more predicted completions along with the probabilities of alternative tokens at each position. Most developer should use our [Chat Completions API](https://platform.openai.com/docs/guides/text-generation/text-generation-models) to leverage our best and newest models.

[

## Create completion

Legacy



](https://platform.openai.com/docs/api-reference/completions/create)

POST https://api.openai.com/v1/completions

Creates a completion for the provided prompt and parameters.

### Request body

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-model)

model

string

Required

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-prompt)

prompt

string or array

Required

The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.

Note that <|endoftext|> is the document separator that the model sees during training, so if a prompt is not specified the model will generate as if from the beginning of a new document.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-best_of)

best_of

integer or null

Optional

Defaults to 1

Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed.

When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return – `best_of` must be greater than `n`.

**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-echo)

echo

boolean or null

Optional

Defaults to false

Echo back the prompt in addition to the completion

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-frequency_penalty)

frequency_penalty

number or null

Optional

Defaults to 0

Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

[See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-logit_bias)

logit_bias

map

Optional

Defaults to null

Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this [tokenizer tool](https://platform.openai.com/tokenizer?view=bpe) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token from being generated.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-logprobs)

logprobs

integer or null

Optional

Defaults to null

Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.

The maximum value for `logprobs` is 5.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-max_tokens)

max_tokens

integer or null

Optional

Defaults to 16

The maximum number of [tokens](https://platform.openai.com/tokenizer) that can be generated in the completion.

The token count of your prompt plus `max_tokens` cannot exceed the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-n)

n

integer or null

Optional

Defaults to 1

How many completions to generate for each prompt.

**Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-presence_penalty)

presence_penalty

number or null

Optional

Defaults to 0

Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

[See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-seed)

seed

integer or null

Optional

If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.

Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-stop)

stop

string / array / null

Optional

Defaults to null

Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-stream)

stream

boolean or null

Optional

Defaults to false

Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-suffix)

suffix

string or null

Optional

Defaults to null

The suffix that comes after a completion of inserted text.

This parameter is only supported for `gpt-3.5-turbo-instruct`.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-temperature)

temperature

number or null

Optional

Defaults to 1

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

We generally recommend altering this or `top_p` but not both.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-top_p)

top_p

number or null

Optional

Defaults to 1

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or `temperature` but not both.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions-create-user)

user

string

Optional

A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

### Returns

Returns a [completion](https://platform.openai.com/docs/api-reference/completions/object) object, or a sequence of completion objects if the request is streamed.

No streaming‍Streaming‍

Example request

gpt-3.5-turbo-instruct

gpt-3.5-turbo-instruct

node.js

Select librarycurlpythonnode.js

```javascript
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
import OpenAI from "openai";

const openai = new OpenAI();

async function main() {
  const completion = await openai.completions.create({
    model: "gpt-3.5-turbo-instruct",
    prompt: "Say this is a test.",
    max_tokens: 7,
    temperature: 0,
  });

  console.log(completion);
}
main();
```

Response

gpt-3.5-turbo-instruct

gpt-3.5-turbo-instruct

```json
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
{
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": "gpt-3.5-turbo-instruct",
  "system_fingerprint": "fp_44709d6fcb",
  "choices": [
    {
      "text": "\n\nThis is indeed a test",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 7,
    "total_tokens": 12
  }
}
```

[

## The completion object

Legacy



](https://platform.openai.com/docs/api-reference/completions/object)

Represents a completion response from the API. Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint).

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions/object-id)

id

string

A unique identifier for the completion.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions/object-choices)

choices

array

The list of completion choices the model generated for the input prompt.

Show properties

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions/object-created)

created

integer

The Unix timestamp (in seconds) of when the completion was created.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions/object-model)

model

string

The model used for completion.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions/object-system_fingerprint)

system_fingerprint

string

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions/object-object)

object

string

The object type, which is always "text_completion"

[](https://platform.openai.com/docs/api-reference/fine-tuning/list-events#completions/object-usage)

usage

object

Usage statistics for the completion request.

Show properties

The completion object

```JSON
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
{
  "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  "object": "text_completion",
  "created": 1589478378,
  "model": "gpt-3.5-turbo",
  "choices": [
    {
      "text": "\n\nThis is indeed a test",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 7,
    "total_tokens": 12
  }
}
```