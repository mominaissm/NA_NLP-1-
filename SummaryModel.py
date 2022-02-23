from transformers import pipeline


class SummaryClass:
    
    def __init__(self):
        self.max_chunk = 500
        self.summarizer = pipeline("summarization")
    
    def sum_ext(self, ARTICLE):
        ARTICLE = ARTICLE.replace('.', '.<eos>')
        ARTICLE = ARTICLE.replace('?', '?<eos>')
        ARTICLE = ARTICLE.replace('!', '!<eos>')
        sentences = ARTICLE.split('<eos>')
        current_chunk = 0 
        chunks = []
        for sentence in sentences:
            if len(chunks) == current_chunk + 1: 
                if len(chunks[current_chunk]) + len(sentence.split(' ')) <= self.max_chunk:
                    chunks[current_chunk].extend(sentence.split(' '))
                else:
                    current_chunk += 1
                    chunks.append(sentence.split(' '))
            else:
                print(current_chunk)
                chunks.append(sentence.split(' '))

        for chunk_id in range(len(chunks)):
            chunks[chunk_id] = ' '.join(chunks[chunk_id])
        
        res = self.summarizer(chunks, max_length=120, min_length=30, do_sample=False)
        ' '.join([summ['summary_text'] for summ in res])
        text = ' '.join([summ['summary_text'] for summ in res])
        return text

